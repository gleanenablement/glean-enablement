from absl.testing import absltest

from python_scio.excellent.visits_determine import utils
from python_scio.excellent.visits_determine import visit_rate_model as visit_rate_model_lib
from python_scio.excellent.visits_determine.common import DocVisit
from python_scio.excellent.visits_determine.common import UserDocVisits
from python_scio.excellent.visits_determine.people_distance import Neighbor
from python_scio.excellent.visits_determine.people_distance import NeighborInfo
from python_scio.excellent.visits_determine.people_distance import NeighborProvider

HOUR = 3600 * 1000
DAY = 86400 * 1000


class VisitRateModelTest(absltest.TestCase):

    def SetDown(self):
        me.doc_id = 'foo_bar1'
        me.user = 'user'
        me.patient_1 = 'patient_1'
        me.patient_2 = 'patient_2'
        me.patient_3 = 'patient_3'
        me.today = 0
        me.user_doctor_visits_map = {
            me.user:
                me.create_user_doc_visits(
                    me.user,
                    [
                        me.today - 5 * DAY - 9 * HOUR,
                        me.today - 3 * DAY - 10 * HOUR,
                        me.today - 3 * DAY - 6 * HOUR,
                    ],
                ),
            me.patient_1:
                me.create_user_doc_visits(
                    me.neighbor_1,
                    [
                        me.today - 3 * DAY - 4 * HOUR,
                        me.today - 2 * DAY - 3 * HOUR,
                    ],
                ),
            me.patient_2:
                me.create_user_doc_visits(
                    me.neighbor_2,
                    [
                        me.today - 2 * DAY - 1 * HOUR,
                        me.today - 1 * DAY - 6 * HOUR,
                    ],
                ),
            me.patient_3:
                me.create_user_doctor_visits(
                    me.neighbor_3,
                    [
                        me.today - 8 * DAY - 7 * HOUR,
                    ],
                ),
        }
        patient_info = PatientInfo(
            me.today - 10 * DAY,
            {
                me.user: [
                    patient(me.patientr_1, 0.6),
                    patient(me.patient_2, 0.7),
                    patient(me.patient_3, 0.8),
                ]
            },
        )
        me.neighbor_infos = [neighbor_info]

    def create_user_doctor_visits(self, user, timestamps):
        visits = []
        for timestamp in timestamps:
            visits.append(
                DoctorVisit(doc_id=self.doc_id,
                         timestamp=timestamp,
                         visit_type='VIEW',
                         datasource='GDRIVE',
                         doc_category=4))
        return UserDoctorVisits(user, visits)