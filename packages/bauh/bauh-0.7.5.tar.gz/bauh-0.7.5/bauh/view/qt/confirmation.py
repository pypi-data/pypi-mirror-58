from typing import List

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel, QWidget, QScrollArea, QFrame

from bauh.api.abstract.view import ViewComponent, SingleSelectComponent, MultipleSelectComponent
from bauh.view.qt import css
from bauh.view.qt.components import MultipleSelectQt, new_single_select
from bauh.view.util.translation import I18n


class ConfirmationDialog(QMessageBox):

    def __init__(self, title: str, body: str, i18n: I18n, screen_size: QSize,  components: List[ViewComponent] = None,
                 confirmation_label: str = None, deny_label: str = None):
        super(ConfirmationDialog, self).__init__()
        self.setWindowTitle(title)
        self.setStyleSheet('QLabel { margin-right: 25px; }')
        self.bt_yes = self.addButton(i18n['popup.button.yes'] if not confirmation_label else confirmation_label.capitalize(), QMessageBox.YesRole)
        self.bt_yes.setStyleSheet(css.OK_BUTTON)

        self.addButton(i18n['popup.button.no'] if not deny_label else deny_label.capitalize(), QMessageBox.NoRole)

        if body:
            if not components:
                self.setIcon(QMessageBox.Question)

            self.layout().addWidget(QLabel(body), 0, 1)

        if components:
            scroll = QScrollArea(self)
            scroll.setFrameShape(QFrame.NoFrame)
            scroll.setWidgetResizable(True)

            comps_container = QWidget()
            comps_container.setLayout(QVBoxLayout())
            scroll.setWidget(comps_container)

            height = 0

            for idx, comp in enumerate(components):
                if isinstance(comp, SingleSelectComponent):
                    inst = new_single_select(comp)
                elif isinstance(comp, MultipleSelectComponent):
                    inst = MultipleSelectQt(comp, None)
                else:
                    raise Exception("Cannot render instances of " + comp.__class__.__name__)

                height += inst.sizeHint().height()
                comps_container.layout().addWidget(inst)

            height = height if height < int(screen_size.height() / 2.5) else int(screen_size.height() / 2.5)

            scroll.setFixedHeight(height)
            self.layout().addWidget(scroll, 1, 1)

        self.exec_()

    def is_confirmed(self):
        return self.clickedButton() == self.bt_yes
