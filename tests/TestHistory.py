import unittest

import commands
import models


class TestHistory(unittest.TestCase):
    def test_get_history(self):
        data = models.HistoryStorage.get_user_history("just-an-dev")
        self.assertEqual(5, len(data))

    def test_update_history(self):
        # get an old tip
        data = models.HistoryStorage.get_user_history("just-an-dev")
        tip_saved = models.Tip().create_from_array(data[1])
        self.assertEqual(42122771, tip_saved.id)

        # update tip info
        tip_saved.finish = True
        tip_saved.tx_id = "transaction id of tip"
        models.HistoryStorage.update_tip('just-an-dev', tip_saved)

        # check of update
        data_verif = models.HistoryStorage.get_user_history("just-an-dev")
        tip_verif = models.Tip().create_from_array(data_verif[1])

        self.assertEqual(42122771, tip_verif.id)
        self.assertEqual(True, tip_verif.finish)
        self.assertEqual("transaction id of tip", tip_verif.tx_id)

    def test_build_history(self):
        data = models.HistoryStorage.get_user_history("just-an-dev")
        commands.history.build_message(data)

    def test_add_history(self):
        user = models.User("just-an-dev")
        models.HistoryStorage.add_to_history(user, "", "", "", "")


if __name__ == '__main__':
    unittest.main()
