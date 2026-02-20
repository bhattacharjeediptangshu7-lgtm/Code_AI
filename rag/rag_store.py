import chromadb
from chromadb.utils import embedding_functions

from config.settings import settings


class RAGStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./rag_db"
        )

        self.embedding = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        self.collection = self.client.get_or_create_collection(

            name="projects",

            embedding_function=self.embedding

        )


    def save_project(self, project_name, files):

        for file_path in files:

            with open(file_path, "r", encoding="utf-8") as f:

                content = f.read()


            self.collection.add(

                documents=[content],

                metadatas=[{"project": project_name}],

                ids=[file_path]

            )