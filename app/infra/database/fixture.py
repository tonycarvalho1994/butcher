from datetime import datetime

MEMORY_DATABASE = {
    'planning': [
        {
            'id_phase': 100,
            'id_patient': '006049',
            'anatomic_location': 'Próstata',
            'intent': 'Radical',
            'modality': 'Teste',
            'technique': '3D',
            'daily_dose_tx': 100,
            'total_dose_tx': 1000,
            'fractions': 10,
            'create_dt': datetime(year=2022, month=6, day=27, hour=12, minute=0, second=0),
            'edit_dt': datetime(year=2022, month=6, day=27, hour=12, minute=0, second=0),
        },
    ],
    'tx_field': [
        {
            'id_field': 1,
            'id_patient': '006049',
            'id_planning': 100,
            'name': '6CGy',
            'number': 1,
            'dose': 30,
            'meter_set': 30,
            'energy': 6,
            'energy_unit_enum': 2,
            'gantry_ang': 100,
            'collimator_ang': 33,
            'couch_ang': 56,
            'create_dt': datetime(year=2022, month=6, day=27, hour=12, minute=1, second=0),
            'edit_dt': datetime(year=2022, month=6, day=27, hour=12, minute=1, second=0),
        },
        {
            'id_field': 2,
            'id_patient': '006049',
            'id_planning': 100,
            'name': '6CGy',
            'number': 1,
            'dose': 70,
            'meter_set': 70,
            'energy': 6,
            'energy_unit_enum': 2,
            'gantry_ang': 198,
            'collimator_ang': 203,
            'couch_ang': 106,
            'create_dt': datetime(year=2022, month=6, day=27, hour=12, minute=2, second=0),
            'edit_dt': datetime(year=2022, month=6, day=27, hour=12, minute=2, second=0),
        },
    ]
}
