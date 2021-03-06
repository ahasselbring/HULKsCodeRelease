# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/mate/ui/views/map/layer/selfPlayer_config_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelfPlayerConfig(object):
    def setupUi(self, SelfPlayerConfig):
        SelfPlayerConfig.setObjectName("SelfPlayerConfig")
        SelfPlayerConfig.resize(945, 912)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelfPlayerConfig)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(SelfPlayerConfig)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 913, 1355))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(4, 4, 4, 4)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.edit_name = QtWidgets.QLineEdit(self.groupBox)
        self.edit_name.setObjectName("edit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_name)
        self.centerLabel = QtWidgets.QLabel(self.groupBox)
        self.centerLabel.setObjectName("centerLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.centerLabel)
        self.centerWidget = QtWidgets.QWidget(self.groupBox)
        self.centerWidget.setObjectName("centerWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centerWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_center_x = QtWidgets.QLabel(self.centerWidget)
        self.label_center_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_center_x.setObjectName("label_center_x")
        self.horizontalLayout_2.addWidget(self.label_center_x)
        self.spin_center_x = QtWidgets.QDoubleSpinBox(self.centerWidget)
        self.spin_center_x.setMinimum(-99.99)
        self.spin_center_x.setObjectName("spin_center_x")
        self.horizontalLayout_2.addWidget(self.spin_center_x)
        self.label_center_y = QtWidgets.QLabel(self.centerWidget)
        self.label_center_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_center_y.setObjectName("label_center_y")
        self.horizontalLayout_2.addWidget(self.label_center_y)
        self.spin_center_y = QtWidgets.QDoubleSpinBox(self.centerWidget)
        self.spin_center_y.setMinimum(-99.99)
        self.spin_center_y.setObjectName("spin_center_y")
        self.horizontalLayout_2.addWidget(self.spin_center_y)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.centerWidget)
        self.enabledLabel = QtWidgets.QLabel(self.groupBox)
        self.enabledLabel.setObjectName("enabledLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.enabledLabel)
        self.enabledCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.enabledCheckBox.setChecked(True)
        self.enabledCheckBox.setObjectName("enabledCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enabledCheckBox)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(4, 4, 4, 4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.poseKeyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.poseKeyLabel.setObjectName("poseKeyLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.poseKeyLabel)
        self.poseKeyLambdaWidget = QtWidgets.QWidget(self.groupBox_2)
        self.poseKeyLambdaWidget.setObjectName("poseKeyLambdaWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.poseKeyLambdaWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cbx_PoseKey = QtWidgets.QComboBox(self.poseKeyLambdaWidget)
        self.cbx_PoseKey.setEditable(True)
        self.cbx_PoseKey.setObjectName("cbx_PoseKey")
        self.verticalLayout_6.addWidget(self.cbx_PoseKey)
        self.label = QtWidgets.QLabel(self.poseKeyLambdaWidget)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.edit_poseKeyLambda = QtWidgets.QTextEdit(self.poseKeyLambdaWidget)
        self.edit_poseKeyLambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.edit_poseKeyLambda.setObjectName("edit_poseKeyLambda")
        self.verticalLayout_6.addWidget(self.edit_poseKeyLambda)
        self.label_2 = QtWidgets.QLabel(self.poseKeyLambdaWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.poseKeyLambdaWidget)
        self.drawPoseLabel = QtWidgets.QLabel(self.groupBox_2)
        self.drawPoseLabel.setObjectName("drawPoseLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.drawPoseLabel)
        self.drawPoseCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.drawPoseCheckBox.setChecked(True)
        self.drawPoseCheckBox.setObjectName("drawPoseCheckBox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.drawPoseCheckBox)
        self.positionCircleDiameterLabel = QtWidgets.QLabel(self.groupBox_2)
        self.positionCircleDiameterLabel.setObjectName("positionCircleDiameterLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.positionCircleDiameterLabel)
        self.spin_positionCircleDiameter = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_positionCircleDiameter.setObjectName("spin_positionCircleDiameter")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_positionCircleDiameter)
        self.orientationLineLengthLabel = QtWidgets.QLabel(self.groupBox_2)
        self.orientationLineLengthLabel.setObjectName("orientationLineLengthLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.orientationLineLengthLabel)
        self.spin_orientationLineLength = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.spin_orientationLineLength.setObjectName("spin_orientationLineLength")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spin_orientationLineLength)
        self.fixedColorLabel = QtWidgets.QLabel(self.groupBox_2)
        self.fixedColorLabel.setObjectName("fixedColorLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.fixedColorLabel)
        self.fixedColorWidget = QtWidgets.QWidget(self.groupBox_2)
        self.fixedColorWidget.setObjectName("fixedColorWidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.fixedColorWidget)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.edit_fixedColor = QtWidgets.QLineEdit(self.fixedColorWidget)
        self.edit_fixedColor.setObjectName("edit_fixedColor")
        self.horizontalLayout_11.addWidget(self.edit_fixedColor)
        self.btn_fixedColor = QtWidgets.QPushButton(self.fixedColorWidget)
        self.btn_fixedColor.setFlat(False)
        self.btn_fixedColor.setObjectName("btn_fixedColor")
        self.horizontalLayout_11.addWidget(self.btn_fixedColor)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.fixedColorWidget)
        self.useFixedColorLabel = QtWidgets.QLabel(self.groupBox_2)
        self.useFixedColorLabel.setObjectName("useFixedColorLabel")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.useFixedColorLabel)
        self.useFixedColorCheckBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.useFixedColorCheckBox.setChecked(False)
        self.useFixedColorCheckBox.setObjectName("useFixedColorCheckBox")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.useFixedColorCheckBox)
        self.roleKeyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.roleKeyLabel.setObjectName("roleKeyLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.roleKeyLabel)
        self.roleKeyLambdaWidget = QtWidgets.QWidget(self.groupBox_2)
        self.roleKeyLambdaWidget.setObjectName("roleKeyLambdaWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.roleKeyLambdaWidget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.cbx_RoleKey = QtWidgets.QComboBox(self.roleKeyLambdaWidget)
        self.cbx_RoleKey.setEditable(True)
        self.cbx_RoleKey.setObjectName("cbx_RoleKey")
        self.verticalLayout_7.addWidget(self.cbx_RoleKey)
        self.label_3 = QtWidgets.QLabel(self.roleKeyLambdaWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.edit_roleKeyLambda = QtWidgets.QTextEdit(self.roleKeyLambdaWidget)
        self.edit_roleKeyLambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.edit_roleKeyLambda.setObjectName("edit_roleKeyLambda")
        self.verticalLayout_7.addWidget(self.edit_roleKeyLambda)
        self.label_4 = QtWidgets.QLabel(self.roleKeyLambdaWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.roleKeyLambdaWidget)
        self.defaultColorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.defaultColorLabel_2.setObjectName("defaultColorLabel_2")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.defaultColorLabel_2)
        self.defaultColorWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.defaultColorWidget_2.setObjectName("defaultColorWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.defaultColorWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edit_defaultColor = QtWidgets.QLineEdit(self.defaultColorWidget_2)
        self.edit_defaultColor.setObjectName("edit_defaultColor")
        self.horizontalLayout_3.addWidget(self.edit_defaultColor)
        self.btn_defaultColor = QtWidgets.QPushButton(self.defaultColorWidget_2)
        self.btn_defaultColor.setFlat(False)
        self.btn_defaultColor.setObjectName("btn_defaultColor")
        self.horizontalLayout_3.addWidget(self.btn_defaultColor)
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.defaultColorWidget_2)
        self.keeperColorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.keeperColorLabel_2.setObjectName("keeperColorLabel_2")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.keeperColorLabel_2)
        self.keeperColorWidget = QtWidgets.QWidget(self.groupBox_2)
        self.keeperColorWidget.setObjectName("keeperColorWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.keeperColorWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.edit_keeperColor = QtWidgets.QLineEdit(self.keeperColorWidget)
        self.edit_keeperColor.setObjectName("edit_keeperColor")
        self.horizontalLayout_4.addWidget(self.edit_keeperColor)
        self.btn_keeperColor = QtWidgets.QPushButton(self.keeperColorWidget)
        self.btn_keeperColor.setFlat(False)
        self.btn_keeperColor.setObjectName("btn_keeperColor")
        self.horizontalLayout_4.addWidget(self.btn_keeperColor)
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.keeperColorWidget)
        self.defenderColorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.defenderColorLabel_2.setObjectName("defenderColorLabel_2")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.defenderColorLabel_2)
        self.defenderColorWidget = QtWidgets.QWidget(self.groupBox_2)
        self.defenderColorWidget.setObjectName("defenderColorWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.defenderColorWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edit_defenderColor = QtWidgets.QLineEdit(self.defenderColorWidget)
        self.edit_defenderColor.setObjectName("edit_defenderColor")
        self.horizontalLayout_5.addWidget(self.edit_defenderColor)
        self.btn_defenderColor = QtWidgets.QPushButton(self.defenderColorWidget)
        self.btn_defenderColor.setFlat(False)
        self.btn_defenderColor.setObjectName("btn_defenderColor")
        self.horizontalLayout_5.addWidget(self.btn_defenderColor)
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.defenderColorWidget)
        self.supporterColorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.supporterColorLabel_2.setObjectName("supporterColorLabel_2")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.supporterColorLabel_2)
        self.supporterColorWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.supporterColorWidget_2.setObjectName("supporterColorWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.supporterColorWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.edit_supporterColor = QtWidgets.QLineEdit(self.supporterColorWidget_2)
        self.edit_supporterColor.setObjectName("edit_supporterColor")
        self.horizontalLayout_6.addWidget(self.edit_supporterColor)
        self.btn_supporterColor = QtWidgets.QPushButton(self.supporterColorWidget_2)
        self.btn_supporterColor.setFlat(False)
        self.btn_supporterColor.setObjectName("btn_supporterColor")
        self.horizontalLayout_6.addWidget(self.btn_supporterColor)
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.supporterColorWidget_2)
        self.strikerColorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.strikerColorLabel_2.setObjectName("strikerColorLabel_2")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.strikerColorLabel_2)
        self.strikerColorWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.strikerColorWidget_2.setObjectName("strikerColorWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.strikerColorWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.edit_strikerColor = QtWidgets.QLineEdit(self.strikerColorWidget_2)
        self.edit_strikerColor.setObjectName("edit_strikerColor")
        self.horizontalLayout_7.addWidget(self.edit_strikerColor)
        self.btn_strikerColor = QtWidgets.QPushButton(self.strikerColorWidget_2)
        self.btn_strikerColor.setFlat(False)
        self.btn_strikerColor.setObjectName("btn_strikerColor")
        self.horizontalLayout_7.addWidget(self.btn_strikerColor)
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.strikerColorWidget_2)
        self.bishopColorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.bishopColorLabel_2.setObjectName("bishopColorLabel_2")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.bishopColorLabel_2)
        self.bishopColorWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.bishopColorWidget_2.setObjectName("bishopColorWidget_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.bishopColorWidget_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.edit_bishopColor = QtWidgets.QLineEdit(self.bishopColorWidget_2)
        self.edit_bishopColor.setObjectName("edit_bishopColor")
        self.horizontalLayout_8.addWidget(self.edit_bishopColor)
        self.btn_bishopColor = QtWidgets.QPushButton(self.bishopColorWidget_2)
        self.btn_bishopColor.setFlat(False)
        self.btn_bishopColor.setObjectName("btn_bishopColor")
        self.horizontalLayout_8.addWidget(self.btn_bishopColor)
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.bishopColorWidget_2)
        self.replacementKeeperColorLabel_2 = QtWidgets.QLabel(self.groupBox_2)
        self.replacementKeeperColorLabel_2.setObjectName("replacementKeeperColorLabel_2")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.replacementKeeperColorLabel_2)
        self.replacementKeeperColorWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.replacementKeeperColorWidget_2.setObjectName("replacementKeeperColorWidget_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.replacementKeeperColorWidget_2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.edit_replacementKeeperColor = QtWidgets.QLineEdit(self.replacementKeeperColorWidget_2)
        self.edit_replacementKeeperColor.setObjectName("edit_replacementKeeperColor")
        self.horizontalLayout_9.addWidget(self.edit_replacementKeeperColor)
        self.btn_replacementKeeperColor = QtWidgets.QPushButton(self.replacementKeeperColorWidget_2)
        self.btn_replacementKeeperColor.setFlat(False)
        self.btn_replacementKeeperColor.setObjectName("btn_replacementKeeperColor")
        self.horizontalLayout_9.addWidget(self.btn_replacementKeeperColor)
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.replacementKeeperColorWidget_2)
        self.verticalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(4, 4, 4, 4)
        self.formLayout_3.setObjectName("formLayout_3")
        self.poseKeyLabel_2 = QtWidgets.QLabel(self.groupBox_3)
        self.poseKeyLabel_2.setObjectName("poseKeyLabel_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.poseKeyLabel_2)
        self.jointSensorDataKeyLambdaWidget = QtWidgets.QWidget(self.groupBox_3)
        self.jointSensorDataKeyLambdaWidget.setObjectName("jointSensorDataKeyLambdaWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.jointSensorDataKeyLambdaWidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cbx_JointSensorDataKey = QtWidgets.QComboBox(self.jointSensorDataKeyLambdaWidget)
        self.cbx_JointSensorDataKey.setEditable(True)
        self.cbx_JointSensorDataKey.setObjectName("cbx_JointSensorDataKey")
        self.verticalLayout_8.addWidget(self.cbx_JointSensorDataKey)
        self.label_5 = QtWidgets.QLabel(self.jointSensorDataKeyLambdaWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.edit_jointSensorDataKeyLambda = QtWidgets.QTextEdit(self.jointSensorDataKeyLambdaWidget)
        self.edit_jointSensorDataKeyLambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.edit_jointSensorDataKeyLambda.setObjectName("edit_jointSensorDataKeyLambda")
        self.verticalLayout_8.addWidget(self.edit_jointSensorDataKeyLambda)
        self.label_6 = QtWidgets.QLabel(self.jointSensorDataKeyLambdaWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.jointSensorDataKeyLambdaWidget)
        self.drawFOVLabel = QtWidgets.QLabel(self.groupBox_3)
        self.drawFOVLabel.setObjectName("drawFOVLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.drawFOVLabel)
        self.drawFOVCheckBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.drawFOVCheckBox.setChecked(True)
        self.drawFOVCheckBox.setObjectName("drawFOVCheckBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.drawFOVCheckBox)
        self.maxDistanceLabel = QtWidgets.QLabel(self.groupBox_3)
        self.maxDistanceLabel.setObjectName("maxDistanceLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.maxDistanceLabel)
        self.spin_maxDistance = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spin_maxDistance.setObjectName("spin_maxDistance")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_maxDistance)
        self.cameraOpeningAngleLabel = QtWidgets.QLabel(self.groupBox_3)
        self.cameraOpeningAngleLabel.setObjectName("cameraOpeningAngleLabel")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.cameraOpeningAngleLabel)
        self.spin_cameraOpeningAngle = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.spin_cameraOpeningAngle.setObjectName("spin_cameraOpeningAngle")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spin_cameraOpeningAngle)
        self.verticalLayout_4.addLayout(self.formLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(4, 4, 4, 4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.poseKeyLabel_3 = QtWidgets.QLabel(self.groupBox_4)
        self.poseKeyLabel_3.setObjectName("poseKeyLabel_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.poseKeyLabel_3)
        self.motionPlannerKeyLambdaWidget = QtWidgets.QWidget(self.groupBox_4)
        self.motionPlannerKeyLambdaWidget.setObjectName("motionPlannerKeyLambdaWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.motionPlannerKeyLambdaWidget)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cbx_MotionPlannerKey = QtWidgets.QComboBox(self.motionPlannerKeyLambdaWidget)
        self.cbx_MotionPlannerKey.setEditable(True)
        self.cbx_MotionPlannerKey.setObjectName("cbx_MotionPlannerKey")
        self.verticalLayout_10.addWidget(self.cbx_MotionPlannerKey)
        self.label_7 = QtWidgets.QLabel(self.motionPlannerKeyLambdaWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.edit_motionPlannerKeyLambda = QtWidgets.QTextEdit(self.motionPlannerKeyLambdaWidget)
        self.edit_motionPlannerKeyLambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.edit_motionPlannerKeyLambda.setObjectName("edit_motionPlannerKeyLambda")
        self.verticalLayout_10.addWidget(self.edit_motionPlannerKeyLambda)
        self.label_8 = QtWidgets.QLabel(self.motionPlannerKeyLambdaWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.motionPlannerKeyLambdaWidget)
        self.drawMotionPlanLabel = QtWidgets.QLabel(self.groupBox_4)
        self.drawMotionPlanLabel.setObjectName("drawMotionPlanLabel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.drawMotionPlanLabel)
        self.drawMotionPlanCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.drawMotionPlanCheckBox.setChecked(True)
        self.drawMotionPlanCheckBox.setObjectName("drawMotionPlanCheckBox")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.drawMotionPlanCheckBox)
        self.targetCircleDiameterLabel = QtWidgets.QLabel(self.groupBox_4)
        self.targetCircleDiameterLabel.setObjectName("targetCircleDiameterLabel")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.targetCircleDiameterLabel)
        self.spin_targetCircleDiameter = QtWidgets.QDoubleSpinBox(self.groupBox_4)
        self.spin_targetCircleDiameter.setObjectName("spin_targetCircleDiameter")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_targetCircleDiameter)
        self.drawTranslationLabel = QtWidgets.QLabel(self.groupBox_4)
        self.drawTranslationLabel.setObjectName("drawTranslationLabel")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.drawTranslationLabel)
        self.drawTranslationCheckBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.drawTranslationCheckBox.setChecked(False)
        self.drawTranslationCheckBox.setObjectName("drawTranslationCheckBox")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.drawTranslationCheckBox)
        self.translationColorLabel_2 = QtWidgets.QLabel(self.groupBox_4)
        self.translationColorLabel_2.setObjectName("translationColorLabel_2")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.translationColorLabel_2)
        self.translationColorWidget = QtWidgets.QWidget(self.groupBox_4)
        self.translationColorWidget.setObjectName("translationColorWidget")
        self.horizontalLayout_91 = QtWidgets.QHBoxLayout(self.translationColorWidget)
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_91.setObjectName("horizontalLayout_91")
        self.edit_translationColor = QtWidgets.QLineEdit(self.translationColorWidget)
        self.edit_translationColor.setObjectName("edit_translationColor")
        self.horizontalLayout_91.addWidget(self.edit_translationColor)
        self.btn_translationColor = QtWidgets.QPushButton(self.translationColorWidget)
        self.btn_translationColor.setFlat(False)
        self.btn_translationColor.setObjectName("btn_translationColor")
        self.horizontalLayout_91.addWidget(self.btn_translationColor)
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.translationColorWidget)
        self.verticalLayout_9.addLayout(self.formLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setContentsMargins(4, 4, 4, 4)
        self.formLayout_5.setObjectName("formLayout_5")
        self.poseKeyLabel_4 = QtWidgets.QLabel(self.groupBox_5)
        self.poseKeyLabel_4.setObjectName("poseKeyLabel_4")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.poseKeyLabel_4)
        self.ballSearchKeyLambdaWidget = QtWidgets.QWidget(self.groupBox_5)
        self.ballSearchKeyLambdaWidget.setObjectName("ballSearchKeyLambdaWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.ballSearchKeyLambdaWidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.cbx_BallSearchKey = QtWidgets.QComboBox(self.ballSearchKeyLambdaWidget)
        self.cbx_BallSearchKey.setEditable(True)
        self.cbx_BallSearchKey.setObjectName("cbx_BallSearchKey")
        self.verticalLayout_12.addWidget(self.cbx_BallSearchKey)
        self.label_9 = QtWidgets.QLabel(self.ballSearchKeyLambdaWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9)
        self.edit_ballSearchKeyLambda = QtWidgets.QTextEdit(self.ballSearchKeyLambdaWidget)
        self.edit_ballSearchKeyLambda.setMaximumSize(QtCore.QSize(16777215, 80))
        self.edit_ballSearchKeyLambda.setObjectName("edit_ballSearchKeyLambda")
        self.verticalLayout_12.addWidget(self.edit_ballSearchKeyLambda)
        self.label_10 = QtWidgets.QLabel(self.ballSearchKeyLambdaWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_12.addWidget(self.label_10)
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ballSearchKeyLambdaWidget)
        self.drawBallSearchLabel = QtWidgets.QLabel(self.groupBox_5)
        self.drawBallSearchLabel.setObjectName("drawBallSearchLabel")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.drawBallSearchLabel)
        self.drawBallSearchCheckBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.drawBallSearchCheckBox.setChecked(True)
        self.drawBallSearchCheckBox.setObjectName("drawBallSearchCheckBox")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.drawBallSearchCheckBox)
        self.searchCircleDiameterLabel = QtWidgets.QLabel(self.groupBox_5)
        self.searchCircleDiameterLabel.setObjectName("searchCircleDiameterLabel")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.searchCircleDiameterLabel)
        self.spin_searchCircleDiameter = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.spin_searchCircleDiameter.setObjectName("spin_searchCircleDiameter")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spin_searchCircleDiameter)
        self.verticalLayout_11.addLayout(self.formLayout_5)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAccept = QtWidgets.QPushButton(SelfPlayerConfig)
        self.btnAccept.setObjectName("btnAccept")
        self.horizontalLayout.addWidget(self.btnAccept)
        self.btnDiscard = QtWidgets.QPushButton(SelfPlayerConfig)
        self.btnDiscard.setObjectName("btnDiscard")
        self.horizontalLayout.addWidget(self.btnDiscard)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SelfPlayerConfig)
        QtCore.QMetaObject.connectSlotsByName(SelfPlayerConfig)
        SelfPlayerConfig.setTabOrder(self.edit_name, self.spin_center_x)
        SelfPlayerConfig.setTabOrder(self.spin_center_x, self.spin_center_y)
        SelfPlayerConfig.setTabOrder(self.spin_center_y, self.enabledCheckBox)
        SelfPlayerConfig.setTabOrder(self.enabledCheckBox, self.drawPoseCheckBox)
        SelfPlayerConfig.setTabOrder(self.drawPoseCheckBox, self.spin_positionCircleDiameter)
        SelfPlayerConfig.setTabOrder(self.spin_positionCircleDiameter, self.spin_orientationLineLength)
        SelfPlayerConfig.setTabOrder(self.spin_orientationLineLength, self.useFixedColorCheckBox)
        SelfPlayerConfig.setTabOrder(self.useFixedColorCheckBox, self.drawFOVCheckBox)
        SelfPlayerConfig.setTabOrder(self.drawFOVCheckBox, self.spin_maxDistance)
        SelfPlayerConfig.setTabOrder(self.spin_maxDistance, self.spin_cameraOpeningAngle)
        SelfPlayerConfig.setTabOrder(self.spin_cameraOpeningAngle, self.drawMotionPlanCheckBox)
        SelfPlayerConfig.setTabOrder(self.drawMotionPlanCheckBox, self.spin_targetCircleDiameter)
        SelfPlayerConfig.setTabOrder(self.spin_targetCircleDiameter, self.drawTranslationCheckBox)
        SelfPlayerConfig.setTabOrder(self.drawTranslationCheckBox, self.btnAccept)
        SelfPlayerConfig.setTabOrder(self.btnAccept, self.btnDiscard)
        SelfPlayerConfig.setTabOrder(self.btnDiscard, self.scrollArea)

    def retranslateUi(self, SelfPlayerConfig):
        _translate = QtCore.QCoreApplication.translate
        SelfPlayerConfig.setWindowTitle(_translate("SelfPlayerConfig", "Form"))
        self.groupBox.setTitle(_translate("SelfPlayerConfig", "General:"))
        self.nameLabel.setText(_translate("SelfPlayerConfig", "Name:"))
        self.centerLabel.setText(_translate("SelfPlayerConfig", "Center"))
        self.label_center_x.setText(_translate("SelfPlayerConfig", "X:"))
        self.label_center_y.setText(_translate("SelfPlayerConfig", "Y:"))
        self.enabledLabel.setText(_translate("SelfPlayerConfig", "Enabled:"))
        self.groupBox_2.setTitle(_translate("SelfPlayerConfig", "Pose:"))
        self.poseKeyLabel.setText(_translate("SelfPlayerConfig", "PoseKey:"))
        self.label.setText(_translate("SelfPlayerConfig", "def parse(input):"))
        self.label_2.setText(_translate("SelfPlayerConfig", "return output"))
        self.drawPoseLabel.setText(_translate("SelfPlayerConfig", "Show pose:"))
        self.positionCircleDiameterLabel.setText(_translate("SelfPlayerConfig", "positionCircleDiameter:"))
        self.orientationLineLengthLabel.setText(_translate("SelfPlayerConfig", "orientationLineLength"))
        self.fixedColorLabel.setText(_translate("SelfPlayerConfig", "Fixed color"))
        self.btn_fixedColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.useFixedColorLabel.setText(_translate("SelfPlayerConfig", "Use fixed color:"))
        self.roleKeyLabel.setText(_translate("SelfPlayerConfig", "roleKey:"))
        self.label_3.setText(_translate("SelfPlayerConfig", "def parse(input):"))
        self.label_4.setText(_translate("SelfPlayerConfig", "return output"))
        self.defaultColorLabel_2.setText(_translate("SelfPlayerConfig", "defaultColor"))
        self.btn_defaultColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.keeperColorLabel_2.setText(_translate("SelfPlayerConfig", "keeperColor"))
        self.btn_keeperColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.defenderColorLabel_2.setText(_translate("SelfPlayerConfig", "defenderColor"))
        self.btn_defenderColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.supporterColorLabel_2.setText(_translate("SelfPlayerConfig", "supporterColor"))
        self.btn_supporterColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.strikerColorLabel_2.setText(_translate("SelfPlayerConfig", "strikerColor"))
        self.btn_strikerColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.bishopColorLabel_2.setText(_translate("SelfPlayerConfig", "bishopColor"))
        self.btn_bishopColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.replacementKeeperColorLabel_2.setText(_translate("SelfPlayerConfig", "replacementKeeperColor"))
        self.btn_replacementKeeperColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.groupBox_3.setTitle(_translate("SelfPlayerConfig", "FOV:"))
        self.poseKeyLabel_2.setText(_translate("SelfPlayerConfig", "JointSensorDataKey:"))
        self.label_5.setText(_translate("SelfPlayerConfig", "def parse(input):"))
        self.label_6.setText(_translate("SelfPlayerConfig", "return output"))
        self.drawFOVLabel.setText(_translate("SelfPlayerConfig", "Show FOV:"))
        self.maxDistanceLabel.setText(_translate("SelfPlayerConfig", "maxDistance"))
        self.cameraOpeningAngleLabel.setText(_translate("SelfPlayerConfig", "cameraOpeningAngle"))
        self.groupBox_4.setTitle(_translate("SelfPlayerConfig", "Motion Plan:"))
        self.poseKeyLabel_3.setText(_translate("SelfPlayerConfig", "MotionPlannerKey:"))
        self.label_7.setText(_translate("SelfPlayerConfig", "def parse(input):"))
        self.label_8.setText(_translate("SelfPlayerConfig", "return output"))
        self.drawMotionPlanLabel.setText(_translate("SelfPlayerConfig", "Show motion plan:"))
        self.targetCircleDiameterLabel.setText(_translate("SelfPlayerConfig", "targetDiameter"))
        self.drawTranslationLabel.setText(_translate("SelfPlayerConfig", "Show translation:"))
        self.translationColorLabel_2.setText(_translate("SelfPlayerConfig", "translationColor"))
        self.btn_translationColor.setText(_translate("SelfPlayerConfig", "Pick"))
        self.groupBox_5.setTitle(_translate("SelfPlayerConfig", "Ball Search:"))
        self.poseKeyLabel_4.setText(_translate("SelfPlayerConfig", "BallSearchKey:"))
        self.label_9.setText(_translate("SelfPlayerConfig", "def parse(input):"))
        self.label_10.setText(_translate("SelfPlayerConfig", "return output"))
        self.drawBallSearchLabel.setText(_translate("SelfPlayerConfig", "Show search position:"))
        self.searchCircleDiameterLabel.setText(_translate("SelfPlayerConfig", "targetDiameter"))
        self.btnAccept.setText(_translate("SelfPlayerConfig", "Accept"))
        self.btnDiscard.setText(_translate("SelfPlayerConfig", "Discard"))

