PLANNING_BASE_QUERY = """
SELECT 
    S.SIT_ID, 
    S.Pat_ID1, 
    Pat.IDA as ID_SISAC,
    S.Site_Name,
    CP.Tx_Intent,
    S.Modality,
    S.Technique,
    S.Dose_Tx,
    S.Dose_Ttl,
    S.Fractions,
    S.Create_DtTm,
    S.Edit_DtTm
FROM Site as S
INNER JOIN vw_PatBro_Demographics as Pat
    ON (S.Pat_ID1 = Pat.Pat_ID1)
INNER JOIN PatCPlan as CP
    ON (Pat.Pat_ID1 = CP.Pat_ID1)
WHERE
    S.Version = 0 
"""

TXFIELD_BASE_QUERY = """
SELECT
    TF.FLD_ID,
    TF.Pat_ID1, 
    Pat.IDA as ID_SISAC,
    TF.SIT_Set_ID,
    TF.Field_Name,
    TF.DisplaySequence,
    TF.Cgray,
    TF.Meterset,
    TFP.Energy,
    TFP.Energy_Unit_Enum,
    TFP.Gantry_Ang,
    TFP.Coll_Ang,
    TFP.Couch_Ang,
    TF.Create_DtTm,
    TF.Edit_DtTm,
    TF.Sanct_DtTm,
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
        AND Pat.IDA = {id_patient}
        """.format(**query_params)

        return query

    elif 'id_planning' in query_params:
        query = PLANNING_BASE_QUERY + """
            AND S.SIT_ID = {id_planning}
            """.format(**query_params)

        return query


def query_get_txfields(query_params: dict) -> str:
    if 'id_patient' in query_params:
        query = TXFIELD_BASE_QUERY + """
        AND TF.IDA = {id_patient}
        """.format(**query_params)

        return query

    elif 'id_planning' in query_params:
        query = TXFIELD_BASE_QUERY + """
            AND TF.SIT_Set_ID = {id_planning}
            """.format(**query_params)

        return query
