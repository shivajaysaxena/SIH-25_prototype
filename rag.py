import chromadb
from config import METADATA_PATH

class PatientRAG:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=METADATA_PATH)
        self.collection = self.client.get_or_create_collection(name="patient_history")

    def add_entry(self, patient_id: str, symptoms: str, response: str):
        doc = f"Symptoms: {symptoms} Response: {response}"
        self.collection.add(
            documents=[doc],
            metadatas=[{"patient_id": patient_id}],
            ids=[f"{patient_id}_{len(self.collection.get(where={'patient_id': patient_id})['ids']) + 1}"]
        )

    def retrieve_history(self, patient_id: str, query: str, top_k: int = 3) -> str:
        results = self.collection.query(
            query_texts=[query],
            where={"patient_id": patient_id},
            n_results=top_k
        )
        if not results['documents']:
            return ""
        history = []
        for doc in results['documents'][0]:
            history.append(doc)
        return " ".join(history)

rag_system = PatientRAG()
