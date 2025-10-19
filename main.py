import os, argparse, requests, pandas as pd
from dotenv import load_dotenv
from transform import normalize_users_df
from loaders import load_postgres_upsert, load_clickhouse

ap = argparse.ArgumentParser()
ap.add_argument("--target", choices=["postgres","clickhouse","none"], default="postgres")
ap.add_argument("--limit", type=int, default=None)
args = ap.parse_args()

load_dotenv()
API_URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/users")

r = requests.get(API_URL, timeout=30)
r.raise_for_status()
data = r.json()
if args.limit:
    data = data[:args.limit]

df = pd.DataFrame(data)
df = normalize_users_df(df)
print(f"[INFO] rows: {len(df)}")
print(df.head())

if args.target == "postgres":
    load_postgres_upsert(df)
elif args.target == "clickhouse":
    load_clickhouse(df)
else:
    print("[INFO] skip load")
