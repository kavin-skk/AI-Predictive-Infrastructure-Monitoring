import os
import chromadb


class ChromaService:

    def __init__(self):

        db_path = os.path.join(
            os.path.dirname(__file__),
            "../vector_db/chroma_db"
        )

        self.client = chromadb.PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name="infrastructure_incidents"
        )

    # -------------------------
    # Add Incident
    # -------------------------

    def add_incident(self, incident_id, incident, metadata=None):

        if metadata is None:
            metadata = {}

        try:

            existing = self.collection.get(ids=[incident_id])

            if len(existing["ids"]) > 0:

                self.collection.update(
                    ids=[incident_id],
                    documents=[incident],
                    metadatas=[metadata]
                )

                return "Incident Updated"

            else:

                self.collection.add(
                    ids=[incident_id],
                    documents=[incident],
                    metadatas=[metadata]
                )

                return "Incident Added"

        except Exception as e:

            return str(e)

    # -------------------------
    # Search Incident
    # -------------------------

    def search_incident(self, query, results=3):

        result = self.collection.query(
            query_texts=[query],
            n_results=results
        )

        return result

    # -------------------------
    # Get All Incidents
    # -------------------------

    def get_all_incidents(self):

        return self.collection.get()

    # -------------------------
    # Delete Incident
    # -------------------------

    def delete_incident(self, incident_id):

        self.collection.delete(
            ids=[incident_id]
        )

    # -------------------------
    # Total Count
    # -------------------------

    def count(self):

        return self.collection.count()

    # -------------------------
    # Clear Database
    # -------------------------

    def clear_database(self):

        data = self.collection.get()

        if len(data["ids"]) > 0:

            self.collection.delete(
                ids=data["ids"]
            )

        return "Database Cleared"