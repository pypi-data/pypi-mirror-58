"""
    PyJAMAS is Just A More Awesome Siesta
    Copyright (C) 2018  Rodrigo Fernandez-Gonzalez (rodrigo.fernandez.gonzalez@utoronto.ca)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from PyQt5 import QtWidgets

import pyjamas.dialogs as dialogs
from .rcallback import RCallback
import pyjamas.rimage.rimclassifier.rimlr as rimlr


class RCBCreateLR(RCallback):
    def cbCreateLR(self, parameters: dict = None, wait_for_thread: bool = False) -> bool:  # Handle IO errors.
        continue_flag = True

        if parameters is None or parameters is False:
            dialog = QtWidgets.QDialog()
            ui = dialogs.logregression.LRDialog()
            ui.setupUi(dialog)

            dialog.exec_()
            dialog.show()

            continue_flag = dialog.result() == QtWidgets.QDialog.Accepted
            parameters = ui.parameters()

            dialog.close()

        if continue_flag:
            self.pjs.batch_classifier.image_classifier = rimlr.lr(parameters)
            self.launch_thread(self.pjs.batch_classifier.fit, {'stop': True}, finished_fn=self.finished_fn,
                               stop_fn=self.stop_fn, wait_for_thread=wait_for_thread)

            return True

        else:
            return False

