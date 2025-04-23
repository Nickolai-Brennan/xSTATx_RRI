# Python version of the RRI Formula blocks from Google Sheets
import numpy as np
import pandas as pd

# Required for HTML export
from IPython.display import HTML

# Tableau Integration Consideration:
# Data exported to CSV or SQL for Tableau dashboards via Snowflake or local staging

# Master Column Schema Reference Table for RRI
RRI_MASTER_COLUMNS = [
    'Player', 'Team', 'Player_Url', 'Team_Logo_Url',
    'ERA', 'xFIP', 'SIERA', 'WHIP', 'BABIP',
    'K/9', 'BB/9', 'K-BB%', 'CSW%', 'SwStr%', 'Soft%', 'Hard%',
    'Clutch', 'IR_Pct', 'aLI', 'pLI', 'gmLI',
    'Stuff+', 'Location+', 'Pitching+',
    'Stf+ FA', 'Stf+ SI', 'Stf+ FC', 'Stf+ FS', 'Stf+ SL', 'Stf+ CU', 'Stf+ CH', 'Stf+ KC', 'Stf+ FO',
    'Top_5_Pitches_Count', 'Top_5_Pitch_Names',
    'Performance', 'Leverage_Usage', 'Stuff_Quality', 'Batted_Ball', 'Clutch_IR',
    'Prospect_Label', 'Prospect_Rank_Score', 'MiLB_Awards_Score', 'MiLB_Perf_Score', 'Prospect',
    'LT_IL_Stints', 'Consistent_IL_Years', 'Injury_Severity', 'Injury_Frequency', 'Injury',
    'Trade_Rumor_Level', 'Trade',
    'Reliever_Role', 'Status', 'Age', 'Age_Penalty',
    'Team_Tier', 'Run_Diff_Score', 'Win_Pct_Score', 'Preseason_Projection', 'Team_Score',
    'RRI_Score', 'RRI_Percentile', 'RRI_Emojis'
]

# Emoji Index Map for RRI Enhancement
EMOJI_MAP = {
    'Elite Command': '🎯',
    'High Velocity': '💨',
    'Top 5% Stuff': '🔥',
    'Cold Blooded': '🧊',
    'Brick Wall': '🧱',
    'Strikeout Machine': '🌀',
    'Run Prevention': '🔒',
    'Top Prospect': '🌟',
    'Injury Concern': '🩹',
    'Trade Rumor': '🔄',
    'Closer': '🔓',
    'High Leverage': '⚔️',
    'Mop Up': '🧼',
    'Playoff Team': '💍',
    'Division Leader': '👑',
    'World Series Contender': '🏆',
    'Top 5% Overall': '🔝',
    'Ace Tier': '🧠',
    'GOAT Tier': '🐐'
}

def validate_rri_dataframe(df):
    print("
🔍 Validating DataFrame columns against RRI master schema...")
    df_columns = set(df.columns)
    expected_columns = set(RRI_MASTER_COLUMNS)

    missing = expected_columns - df_columns
    extra = df_columns - expected_columns

    if not missing and not extra:
        print("✅ DataFrame is fully compliant with RRI_MASTER_COLUMNS.")
    else:
        if missing:
            print("⚠️ Missing columns:", sorted(missing))
        if extra:
            print("⚠️ Extra/unexpected columns:", sorted(extra))

    return {
        "missing": sorted(missing),
        "extra": sorted(extra),
        "valid": not missing and not extra
    }

def load_rri_from_csv(path):
    print(f"📂 Loading RRI data from: {path}")
    try:
        df = pd.read_csv(path)
        print(f"✅ Successfully loaded {len(df)} rows.")
        validation = validate_rri_dataframe(df)
        if not validation['valid']:
            print("⚠️ DataFrame is missing or contains extra columns.")
        return df
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return pd.DataFrame()

# ... [existing code continues below this]
