import json

import boto3

S3_BUCKET = "hero-files"
DYNAMO_TABLE = "hero-powers"


class HeroVault:
    def __init__(self) -> None:
        self.s3 = boto3.client("s3", region_name="us-east-1")
        self.dynamo = boto3.resource("dynamodb", region_name="us-east-1")
        self.table = self.dynamo.Table(DYNAMO_TABLE)

    # ─── S3 ───────────────────────────────────────────────────────────────────

    def upload_hero_profile(self, hero_name: str, profile: dict) -> str:
        key = f"heroes/{hero_name.lower().replace(' ', '-')}.json"
        self.s3.put_object(
            Bucket=S3_BUCKET,
            Key=key,
            Body=json.dumps(profile),
            ContentType="application/json",
        )
        return key

    def get_hero_profile(self, hero_name: str) -> dict | None:
        key = f"heroes/{hero_name.lower().replace(' ', '-')}.json"
        try:
            response = self.s3.get_object(Bucket=S3_BUCKET, Key=key)
            return json.loads(response["Body"].read())
        except self.s3.exceptions.NoSuchKey:
            return None

    def list_hero_profiles(self) -> list[str]:
        response = self.s3.list_objects_v2(Bucket=S3_BUCKET, Prefix="heroes/")
        contents = response.get("Contents", [])
        return [obj["Key"] for obj in contents]  # type: ignore

    # ─── DynamoDB ─────────────────────────────────────────────────────────────

    def save_powers(self, hero_name: str, powers: dict) -> None:
        self.table.put_item(Item={"hero_name": hero_name, **powers})

    def get_powers(self, hero_name: str) -> dict | None:
        response = self.table.get_item(Key={"hero_name": hero_name})
        return response.get("Item")

    def update_power(self, hero_name: str, power_key: str, value: int) -> dict:
        response = self.table.update_item(
            Key={"hero_name": hero_name},
            UpdateExpression="SET #pk = :val",
            ExpressionAttributeNames={"#pk": power_key},
            ExpressionAttributeValues={":val": value},
            ReturnValues="ALL_NEW",
        )
        return response["Attributes"]
