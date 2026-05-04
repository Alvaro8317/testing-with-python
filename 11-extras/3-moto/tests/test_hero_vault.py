import json

import boto3
from moto import mock_aws
from src import hero_vault


@mock_aws
def test_should_upload_hero_profile_to_s3() -> None:
    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=hero_vault.S3_BUCKET)

    vault = hero_vault.HeroVault()
    profile = {"alias": "Spider-Man", "city": "New York"}
    key = vault.upload_hero_profile("Peter Parker", profile)

    assert key == "heroes/peter-parker.json"
    body = conn.get_object(Bucket=hero_vault.S3_BUCKET, Key=key)["Body"].read()
    assert json.loads(body) == profile


@mock_aws
def test_should_get_existing_hero_profile_from_s3() -> None:
    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=hero_vault.S3_BUCKET)

    vault = hero_vault.HeroVault()
    profile = {"alias": "Iron Man", "city": "Malibu"}
    vault.upload_hero_profile("Tony Stark", profile)

    result = vault.get_hero_profile("Tony Stark")

    assert result == profile


@mock_aws
def test_should_return_none_when_hero_profile_does_not_exist() -> None:
    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=hero_vault.S3_BUCKET)

    vault = hero_vault.HeroVault()
    result = vault.get_hero_profile("Unknown Hero")

    assert result is None


@mock_aws
def test_should_list_all_hero_profiles_in_s3() -> None:
    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=hero_vault.S3_BUCKET)

    vault = hero_vault.HeroVault()
    vault.upload_hero_profile("Thor Odinson", {"alias": "Thor"})
    vault.upload_hero_profile("Bruce Banner", {"alias": "Hulk"})

    keys = vault.list_hero_profiles()

    assert sorted(keys) == sorted(
        [
            "heroes/thor-odinson.json",
            "heroes/bruce-banner.json",
        ]
    )


@mock_aws
def test_should_return_empty_list_when_no_hero_profiles_exist() -> None:
    conn = boto3.client("s3", region_name="us-east-1")
    conn.create_bucket(Bucket=hero_vault.S3_BUCKET)

    vault = hero_vault.HeroVault()
    result = vault.list_hero_profiles()

    assert result == []


@mock_aws
def test_should_save_powers_to_dynamodb() -> None:
    boto3.resource("dynamodb", region_name="us-east-1").create_table(
        TableName=hero_vault.DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "hero_name", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "hero_name", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    vault = hero_vault.HeroVault()
    vault.save_powers("Steve Rogers", {"strength": 95, "speed": 80})

    table = boto3.resource("dynamodb", region_name="us-east-1").Table(hero_vault.DYNAMO_TABLE)
    item = table.get_item(Key={"hero_name": "Steve Rogers"}).get("Item")
    assert item
    assert item["strength"] == 95
    assert item["speed"] == 80


@mock_aws
def test_should_get_powers_from_dynamodb() -> None:
    boto3.resource("dynamodb", region_name="us-east-1").create_table(
        TableName=hero_vault.DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "hero_name", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "hero_name", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    vault = hero_vault.HeroVault()
    vault.save_powers("Wanda Maximoff", {"magic": 100, "telepathy": 90})

    result = vault.get_powers("Wanda Maximoff")
    assert result
    assert result["magic"] == 100
    assert result["telepathy"] == 90


@mock_aws
def test_should_return_none_when_hero_powers_do_not_exist() -> None:
    boto3.resource("dynamodb", region_name="us-east-1").create_table(
        TableName=hero_vault.DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "hero_name", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "hero_name", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    vault = hero_vault.HeroVault()
    result = vault.get_powers("Ghost Hero")

    assert result is None


@mock_aws
def test_should_update_existing_power_in_dynamodb() -> None:
    boto3.resource("dynamodb", region_name="us-east-1").create_table(
        TableName=hero_vault.DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "hero_name", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "hero_name", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    vault = hero_vault.HeroVault()
    vault.save_powers("Natasha Romanoff", {"agility": 85, "stealth": 90})

    updated = vault.update_power("Natasha Romanoff", "agility", 95)

    assert updated["agility"] == 95
    assert updated["stealth"] == 90


@mock_aws
def test_should_return_all_attributes_after_updating_power() -> None:
    boto3.resource("dynamodb", region_name="us-east-1").create_table(
        TableName=hero_vault.DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "hero_name", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "hero_name", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    vault = hero_vault.HeroVault()
    vault.save_powers("Clint Barton", {"aim": 99, "reflexes": 88})

    updated = vault.update_power("Clint Barton", "reflexes", 95)

    assert updated["hero_name"] == "Clint Barton"
    assert updated["aim"] == 99
    assert updated["reflexes"] == 95
