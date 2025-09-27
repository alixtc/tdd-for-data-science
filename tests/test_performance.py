
import pandas as pd
import polars as pl

from load_data import data_loader

emissions = data_loader()
emissions_pandas = (
    emissions.filter(pl.col.electric_range_km.is_null()).collect().to_pandas()
)


def bad_pandas_code():
    df = emissions_pandas
    df = df.dropna(subset=["fuel_consumption"])
    df.drop(["obfcm_data_source", "registered_category"], axis=1, inplace=True)

    df[df["fuel_type"] == "PETROL"]["fuel_type"] = "petrol"
    df["fuel_consumption_per_100km"] = df["fuel_consumption"] * 100

    grouped = []
    for manufacturer in df["manufacturer_name"].unique():
        manuf_df = df[df["manufacturer_name"] == manufacturer]
        for year in df["year"].unique():
            subset_df = manuf_df[(manuf_df["year"] == year)]
            result = {
                "manufacturer_name": manufacturer,
                "year": year,
                "mean_fuel_consumption": subset_df["fuel_consumption_per_100km"].mean(),
                "mean_electric_range": subset_df["electric_range_km"].mean(),
                "vehicle_count": subset_df["vehicle_id"].nunique(),
            }
            grouped.append(result)

    grouped = pd.DataFrame(grouped)
    grouped = grouped.dropna()
    grouped = grouped.sort_values(["mean_fuel_consumption", "year"], ascending=False)
    grouped = grouped[grouped["vehicle_count"] >= 100]
    grouped = grouped.reset_index(drop=True)
    return grouped


def good_pandas_code():
    return (
        emissions_pandas.dropna(subset=["fuel_consumption"])
        .drop(["obfcm_data_source", "registered_category"], axis=1)
        .assign(
            fuel_type=lambda df: df["fuel_type"].replace({"PETROL": "petrol"}),
            fuel_consumption_per_100km=lambda df: df["fuel_consumption"] * 100,
        )
        .groupby(["manufacturer_name", "year"])
        .agg(
            mean_fuel_consumption=("fuel_consumption_per_100km", "mean"),
            mean_electric_range=("electric_range_km", "mean"),
            vehicle_count=("vehicle_id", "nunique"),
        )
        .reset_index()
        .sort_values(["mean_fuel_consumption", "year"], ascending=False)
        .loc[lambda df: df["vehicle_count"] >= 100]
        .reset_index(drop=True)
    )


emissions_polars = pl.DataFrame(emissions_pandas)


def good_polars_code():
    return (
        emissions_polars.drop_nulls(subset=["fuel_consumption"])
        .drop(["obfcm_data_source", "registered_category"])
        .with_columns(
            fuel_type=pl.col.fuel_type.replace({"PETROL": "petrol"}),
            fuel_consumption_per_100km=pl.col.fuel_consumption * 100,
        )
        .group_by("manufacturer_name", "year")
        .agg(
            mean_fuel_consumption=pl.col.fuel_consumption_per_100km.mean(),
            mean_electric_range=pl.col.electric_range_km.mean(),
            vehicle_count=pl.col.vehicle_id.n_unique().cast(pl.Int64),
        )
        .sort(["mean_fuel_consumption", "year"], descending=True)
        .filter(pl.col.vehicle_count >= 100)
    )


def test_bad_pandas_code(benchmark):
    benchmark(bad_pandas_code)

def test_good_pandas_code(benchmark):
    benchmark(good_pandas_code)

def test_good_polars_code(benchmark):
    benchmark(good_polars_code)
