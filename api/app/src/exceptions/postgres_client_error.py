class ModelNotFoundError(Exception):
    def __init__(self, model_name: str, model_id: int):
        self.message = f"{model_name} with id {model_id} not found"
        super().__init__(self.message)