run:
	uvicorn src.main:app --reload 
dev-run:
	ENV_STATE=dev uvicorn src.main:app --reload 
prod-run:
	ENV_STATE=prod uvicorn src.main:app --reload 