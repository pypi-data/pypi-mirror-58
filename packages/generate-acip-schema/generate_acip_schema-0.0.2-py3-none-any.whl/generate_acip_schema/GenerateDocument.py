import json
from socket import timeout
from http.client import IncompleteRead
import logging
from urllib import error, request


class GenerateDocument:
    def __init__(self, doc_number, config, level, collection, fetch_iiif=False):
        self.update_document_with_iiif = fetch_iiif
        self.id = doc_number.split(":")[1] if doc_number.split(":")[0] == "bdr" else doc_number
        self.id_acip = doc_number if doc_number.split(":")[0] == "bdr" else f"bdr:{doc_number}"
        self.config = config
        self.metadata = {"level": level, "collection": collection }
        self.index_name = self.assign_index()
        self.document = self.get_updated_document()
        self.related_ids = self.get_related_ids()

    def get_document(self):
        return self.load_document()

    def get_updated_document(self):

        temp_doc = self.load_document()
        document = self.update_document(temp_doc)
        del temp_doc

        document["_distance"] = self.metadata["level"]
        document["_collection"] = self.metadata["collection"]

        if 'workHasItem' in document:
            if self.update_document_with_iiif:
                iiif = self.get_iiif(document)
                if iiif:
                    document['_manifestURL'] = iiif["manifestURL"]
                    document['_firstImageURL'] = iiif["imageURL"]

        if 'skos:prefLabel' in document:
            document['_label'] = self.inject_pref_label(document['skos:prefLabel'])

        return document

    def get_iiif(self, document):
        iiif = {}
        manifest = self.load_manifest(document['workHasItem'])
        first_image = self.load_first_image_url(manifest)

        if manifest or first_image:
            iiif = {"manifestURL": manifest, "imageURL": first_image}

        return iiif

    def get_related_ids(self):
        full_listing = sorted(self.walk_document(self.document))
        unique_listing = []
        for n, item in enumerate(full_listing):
            if item not in full_listing[n + 1:]:
                unique_listing.append(item)

        return unique_listing

    # example of switch case in python
    def assign_index(self):
        key = self.id[0]
        index_name = f"v{self.metadata['collection']}{self.config['es_index_prefix']}"
        return {
            'W': index_name + "work",
            'I': index_name + "item",
            'P': index_name + "person",
            'G': index_name + "geography",
            'T': index_name + "topic"
        }.get(key, "invalid")

    def load_document(self, doc_number=None, req_obj=None):
        document = None
        making_some_attempts = 0
        _id = self.id if doc_number is None else doc_number
        req = self.config["endpoint"] + _id + self.config["file_type"] if req_obj is None else req_obj

        while making_some_attempts < 10:
            try:
                document = json.load(request.urlopen(req))
                making_some_attempts = 10
            except IncompleteRead as Incomplete_error:
                logging.error(f"error during chunk read {Incomplete_error}")
                making_some_attempts += 1
                continue
            except timeout as Timeout_error:
                logging.error(f"socket timeout {Timeout_error}")
                making_some_attempts += 1
                continue
            except error.HTTPError as HTTP_error:
                logging.error(f"error during url request {HTTP_error.code}")
                making_some_attempts += 1
                continue
            except error.URLError as URL_error:
                logging.error(f"error during url request {URL_error}")
                making_some_attempts += 1
                continue
            break

        return document

    def update_document(self, document):
        updated_document = {}
        if document is not None:
            if '@id' in document:
                if document['@id'] == f"bdr:{self.id}":
                    return document

            if '@graph' in document:
                graph = document['@graph']
                try:
                    root_index = [x['@id'] for x in graph].index(f"bdr:{self.id}")
                except ValueError:
                    root_index = -1

                if root_index > -1:
                    # schema has changed, now document has root @graph with list
                    updated_document = graph[root_index]

                try:
                    author_index = [x['type'] for x in graph].index("AgentAsCreator")
                except ValueError:
                    author_index = -1

                if author_index > -1:
                    if 'agent' in graph[author_index]:
                        updated_document['_creator'] = graph[author_index]['agent']['@id']

                try:
                    notes = [item['noteText'] for item in graph
                             if item.get('type') and item.get('noteText') and item['type'] == 'Note']
                except ValueError:
                    notes = []

                if len(notes) > 0:
                    updated_document['_notes'] = notes

        return updated_document

    def walk_document(self, document, results_listing=None):
        if results_listing is None:
            results_listing = []
        # if node is a dictionary
        if isinstance(document, dict):
            for key, item in document.items():
                # if value is also a dict or list, recurse
                if isinstance(item, (dict, list)):
                    self.walk_document(item, results_listing)
                else:
                    if item != self.id_acip:
                        if self.test_for_identifier(item):
                            results_listing.append(item)

        # if node is a list
        elif isinstance(document, list):
            for i, n in enumerate(document):
                # if value is a dict or list, recurse
                if isinstance(n, (dict, list)):
                    self.walk_document(n, results_listing)
                else:
                    if n != self.id_acip:
                        if self.test_for_identifier(n):
                            results_listing.append(n)

        else:
            logging.error(f"Not Iterable {document}")

        return results_listing

    def load_manifest(self, node):

        manifest = None
        doc_number = node.split(":")[1] if node.split(":")[0] == "bdr" else node

        manifest_document = self.load_document(doc_number=doc_number)

        if 'itemVolumes' in manifest_document and manifest_document is not None:
            if manifest_document['itemVolumes'] == 1:
                if 'itemHasVolume' in manifest_document:
                    manifest = f"{self.config['presentation_endpoint']}/v:{manifest_document['itemHasVolume']}/manifest"
            elif manifest_document['itemVolumes'] > 1:
                manifest = f"{self.config['presentation_endpoint']}/collection/i:{manifest_document['@id']}"

        return manifest

    def load_first_image_url(self, manifest):

        first_image = None
        data = self.load_document(req_obj=manifest)

        if data is not None:
            # this logic taken directly from BDRC
            if 'sequences' not in data:
                if 'manifests' in data:
                    first_image = self.load_first_image_url(data['manifests'][0]['@id'])

            if 'sequences' in data and data['sequences'][0]['canvases']:
                for i in range(len(data['sequences'][0]['canvases'])):
                    s = data['sequences'][0]['canvases'][i]
                    if s['label'] == "tbrc-1":
                        # data['sequences'][0]['canvases'][2]
                        if s['images'][0]:
                            first_image = s['images'][0]['resource']['@id'].split("/full", 1)[0]

                if data['sequences'][0]['canvases'][0]:
                    s = data['sequences'][0]['canvases'][0]
                    if s['images'][0] and s['images'][0]['resource']['@id']:
                        first_image = s['images'][0]['resource']['@id'].split("/full", 1)[0]

        return first_image

    # ###################################
    # Test for bdr prefix and schema type
    # ###################################
    def test_for_identifier(self, s):
        if type(s) == str:
            if s.split(":")[0] == "bdr":
                if s[4] in self.config["indices_of_interest"]:
                    if s[5].isdigit():
                        return True

    # ##########################################
    # Add label to document using skos:prefLabel
    # ##########################################
    def inject_pref_label(self, node):
        label = None
        # if node is a dictionary
        if isinstance(node, dict):
            for key, value in node.items():
                if key == '@value':
                    label = value
        elif isinstance(node, list):
            for item in node:
                if isinstance(item, dict):
                    label = next((item["@value"] for k, v in item.items() if v in self.config["languages_main"]), None)

        return label
