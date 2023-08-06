import json
import logging
from elasticsearch import Elasticsearch, helpers, RequestError, TransportError, ConflictError  # , NotFoundError


class ElasticSearch:
    def __init__(self, config, env):
        self.config = config
        self.environment = env
        self.client = self.create_client()

    def create_client(self):
        return Elasticsearch(
            [self.config[self.environment]],
            sniff_on_start=True,
            # refresh nodes after a node fails to respond
            sniff_on_connection_fail=True,
            # and also every 60 seconds
            sniffer_timeout=60,
            retry_on_timeout=True
        )

    def check_index(self, idx):
        if not self.client.indices.exists(idx):
            print("Creating INDEX", idx)
            self.client.indices.create(idx)

    def recreate_indices(self, collection=""):
        wild_card_indices = f"v{collection}{self.config['index_prefix']}*"
        target_indices = self.client.indices.get_alias(wild_card_indices)
        for i in target_indices:
            print("Deleting index", i)
            self.client.indices.delete(i)

    # ####################
    # Direct index of main works to a FrontEnd index specifically for the UI
    # need to work on how to create this, but for now there's a _resources leaf
    # with all bdr: ID's that resource needs
    # ####################
    def direct_index(self, document, index_name):

        if '@id' not in document:
            raise KeyError

        try:
            self.client.create(
                index=index_name,
                doc_type=self.config["type"],
                body=json.dumps(document),
                id=document['@id']
            )

        except RequestError as e:
            logging.error(f"Request Error during index {e}")
            pass
        except TransportError as e:
            logging.error(f"Transport Error during index {e}")
            pass
        except KeyError as e:
            logging.error(f"Key Error, @id not present on node, {e}")
            pass
