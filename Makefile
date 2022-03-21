run:
	uvicorn app.main:app --reload 
dev-run:
	ENV_STATE=dev uvicorn app.main:app --reload 
prod-run:
	ENV_STATE=prod uvicorn app.main:app --reload 