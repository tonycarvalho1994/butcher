PLANNING_BASE_QUERY = """
SELECT DISTINCT
    S.SIT_ID as id_phase, 
    Pat.IDA as id_patient, 
    S.Site_Name as anatomic_location,
    CP.Tx_Intent as intent,
    S.Modality as modality,
    S.Technique as technique,
    S.Dose_Tx as daily_dose_tx,
    S.Dose_Ttl as total_dose_tx,
    S.Fractions as fractions,
    S.Create_DtTm as create_dt,
    S.Edit_DtTm as edit_dt
FROM Site as S
INNER JOIN vw_PatBro_Demographics as Pat
    ON (S.Pat_ID1 = Pat.Pat_ID1)
INNER JOIN PatCPlan as CP
    ON (Pat.Pat_ID1 = CP.Pat_ID1)
WHERE
    S.Version = 0 
"""

TXFIELD_BASE_QUERY = """
SELECT DISTINCT
    TF.FLD_ID as id_field,
    Pat.IDA as id_patient,
    TF.SIT_Set_ID as id_planning,
    TF.Field_Name as name,
    TF.DisplaySequence as number,
    TF.Cgray as dose,
    TF.Meterset as meter_set,
    TFP.Energy as energy,
    TFP.Energy_Unit_Enum as energy_unit_enum,
    TFP.Gantry_Ang as gantry_ang,
    TFP.Coll_Ang as collimator_ang,
    TFP.Couch_Ang as couch_ang,
    TF.Create_DtTm as create_dt,
    TF.Edit_DtTm as edit_dt
FROM TxField as TF
INNER JOIN vw_PatBro_Demographics as Pat
    ON (TF.Pat_ID1 = Pat.Pat_ID1)
INNER JOIN TxFieldPoint as TFP
    ON (TF.FLD_ID = TFP.FLD_ID)
WHERE TF.Version = 0 
"""


def query_get_plannings(query_params: dict) -> str:
    if 'id_patient' in query_params:
        query = PLANNING_BASE_QUERY + """
        AND Pat.IDA = '{id_patient}'
        """.format(**query_params)

        return query

    elif 'id_planning' in query_params:
        query = PLANNING_BASE_QUERY + """
            AND S.SIT_ID = '{id_planning}'
            """.format(**query_params)

        return query


def query_get_txfields(query_params: dict) -> str:
    if 'id_patient' in query_params:
        query = TXFIELD_BASE_QUERY + """
        AND TF.IDA = '{id_patient}'
        """.format(**query_params)

        return query

    elif 'id_planning' in query_params:
        query = TXFIELD_BASE_QUERY + """
            AND TF.SIT_Set_ID = '{id_planning}'
            """.format(**query_params)

        return query
