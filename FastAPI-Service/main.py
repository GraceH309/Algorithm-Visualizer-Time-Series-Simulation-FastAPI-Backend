# Lightweight data query & batch compute backend with FastAPI
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np

app = FastAPI(title="Data Processing Service")

# Cross origin setup: restrict origin in real production, * only for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mock in-memory sequential dataset, replaced with database in real use
mock_time_data = pd.DataFrame({
    "time_id": list(range(1, 51)),
    "measure": np.random.randint(10, 90, size=50)
})

# Get single record by time id
@app.get("/data/single")
def get_single_record(time_id: int = Query(..., description="target time point id")):
    # simple input boundary check
    if time_id < 1 or time_id > 50:
        raise HTTPException(status_code=400, detail="time_id must be between 1 and 50")
        
    target_row = mock_time_data[mock_time_data["time_id"] == time_id]
    if target_row.empty:
        raise HTTPException(status_code=404, detail="No matching record found")
        
    return {"status": "success", "data": target_row.to_dict("records")[0]}

# Batch calculate metrics within time range
@app.get("/data/batch-metric")
def batch_calc(start: int, end: int):
    # basic param validation
    if start > end or start < 1 or end > 50:
        raise HTTPException(status_code=400, detail="Invalid start/end range")
        
    slice_data = mock_time_data[(mock_time_data["time_id"] >= start) & (mock_time_data["time_id"] <= end)]
    if slice_data.empty:
        return {"status": "empty range", "metrics": None}
        
    avg = slice_data["measure"].mean()
    total = slice_data["measure"].sum()
    return {
        "status": "success",
        "metrics": {"average": round(avg, 2), "sum": total}
    }

if __name__ == "__main__":
    import uvicorn
    # use 0.0.0.0 if you need external network access, 127.0.0.1 only local machine
    uvicorn.run(app, host="127.0.0.1", port=8000)