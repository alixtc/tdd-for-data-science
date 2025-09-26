import polars as pl

EMISSION_SCHEMA = {
    "Vehicle Identifier": pl.Int64,
    "OBFCM data source": pl.String,
    "OBFCM ReportingPeriod": pl.Int64,
    "Total fuel consumed (lifetime) (l)": pl.Float64,
    "Total distance travelled (lifetime) (km)": pl.Float64,
    "Total distance travelled in charge depleting operation with engine off (lifetime) (km)": pl.Float64,
    "Total distance travelled in charge depleting operation with engine running (lifetime) (km)": pl.Float64,
    "Total distance travelled in driver-selectable charge increasing operation (lifetime) (km)": pl.Float64,
    "Total fuel consumed in charge depleting operation (lifetime) (l)": pl.Float64,
    "Total fuel consumed in driver-selectable charge increasing operation (lifetime) (l)": pl.Float64,
    "Total grid energy into the battery (lifetime) (kWh)": pl.Float64,
    "Country": pl.String,
    "VFN": pl.String,
    "Mh": pl.String,
    "T": pl.String,
    "Va": pl.String,
    "Ve": pl.String,
    "Mk": pl.String,
    "Cn": pl.String,
    "Cr": pl.String,
    "M (kg)": pl.Float64,
    "Mt": pl.Float64,
    "Ewltp (g/km)": pl.Float64,
    "Ft": pl.String,
    "Fm": pl.String,
    "Ec (cm3)": pl.Float64,
    "Ep (KW)": pl.Float64,
    "Z (Wh/km)": pl.Float64,
    "Year": pl.Int64,
    "Fuel consumption": pl.Float64,
    "Electric range (km)": pl.Float64,
    "Used in calculation": pl.Int64,
}


def data_loader() -> pl.LazyFrame:
    return (
        pl.scan_csv(
            "data/2023_Cars_Raw.csv",
            schema=EMISSION_SCHEMA,
            null_values=["NULL"],
        )
        .drop(
            "Total distance travelled in charge depleting operation with engine off (lifetime) (km)",
            "Total distance travelled in charge depleting operation with engine running (lifetime) (km)",
            "Total distance travelled in driver-selectable charge increasing operation (lifetime) (km)",
            "Total fuel consumed in charge depleting operation (lifetime) (l)",
            "Total fuel consumed in driver-selectable charge increasing operation (lifetime) (l)",
            "Total grid energy into the battery (lifetime) (kWh)",
        )
        .rename(
            {
                "Vehicle Identifier": "vehicle_id",
                "OBFCM data source": "obfcm_data_source",
                "OBFCM ReportingPeriod": "reporting_period",
                "Total fuel consumed (lifetime) (l)": "total_fuel_consumed_l",
                "Total distance travelled (lifetime) (km)": "total_distance_travelled_km",
                "Country": "country",
                "VFN": "vehicle_family_number",
                "Mh": "manufacturer_name",
                "T": "model_type",
                "Va": "model_variant",
                "Ve": "license_plate",
                "Mk": "brand_name",
                "Cn": "commercial_name",
                "Cr": "registered_category",
                "M (kg)": "mass_kg",
                "Mt": "wltp_test_mass",
                "Ewltp (g/km)": "ewltp_g_per_km",
                "Ft": "fuel_type",
                "Fm": "fuel_mode",
                "Ec (cm3)": "engine_capacity_cm3",
                "Ep (KW)": "engine_power_kw",
                "Z (Wh/km)": "electric_consumption_wh_per_km",
                "Year": "year",
                "Fuel consumption": "fuel_consumption",
                "Electric range (km)": "electric_range_km",
                "Used in calculation": "used_in_calculation",
            }
        )
    )
