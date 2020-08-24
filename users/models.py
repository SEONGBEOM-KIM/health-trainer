import uuid
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    NUMBER_FIRST = 1
    NUMBER_SECOND = 2
    NUMBER_THIRD = 3
    NUMBER_FOURTH = 4
    NUMBER_FIFTH = 5
    NUMBER_SIXTH = 6

    NUMBER_CHOICES = (
        (NUMBER_FIRST, 1),
        (NUMBER_SECOND, 2),
        (NUMBER_THIRD, 3),
        (NUMBER_FOURTH, 4),
        (NUMBER_FIFTH, 5),
        (NUMBER_SIXTH, 6),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    name = models.CharField(max_length=20, blank=True)
    school = models.CharField(max_length=10, blank=True)
    grade = models.IntegerField(choices=NUMBER_CHOICES, blank=True, null=True)
    group = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True, null=True
    )
    teacher = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    # PAPS Events
    pacer = models.IntegerField(blank=True, null=True, default=0)
    longTimeRun = models.IntegerField(blank=True, null=True, default=0)
    stepTest = models.IntegerField(blank=True, null=True, default=0)
    bendFoward = models.IntegerField(blank=True, null=True, default=0)
    totalFlexibility = models.IntegerField(blank=True, null=True, default=0)
    pushUp = models.IntegerField(blank=True, null=True, default=0)
    sitUp = models.IntegerField(blank=True, null=True, default=0)
    grip = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=0
    )
    sprint = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, default=0
    )
    longJump = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True, default=0
    )
    height = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    weight = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    fat = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True, null=True, default=0
    )

    def endurance_point(self):
        if self.pacer == None:
            self.pacer = 0
            return self.pacer

        if self.longTimeRun == None:
            self.longTimeRun = 0
            return self.longTimeRun

        if self.stepTest == None:
            self.stepTest = 0
            return self.stepTest

        endurance_point = 0
        if self.pacer == 0 and self.longTimeRun == 0:
            if self.stepTest == 0:
                return "측정 결과를 입력하세요"

        if self.pacer:
            if self.longTimeRun or self.stepTest:
                return "한 종목만 입력하세요"
            else:
                endurance_point = self.pacer
                if self.grade == 5 and self.gender == "male":
                    # 5학년 남학생 왕복오래달리기 기준 입력
                    if endurance_point >= 100:
                        endurance_point = 1
                        return endurance_point
                    elif endurance_point >= 73 and endurance_point < 100:
                        endurance_point = 2
                        return endurance_point
                    elif endurance_point >= 50 and endurance_point < 73:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 29 and endurance_point < 50:
                        endurance_point = 4
                        return endurance_point
                    else:
                        endurance_point = 5
                        return endurance_point
                    return endurance_point
                if self.grade == 5 and self.gender == "female":
                    # 5학년 여학생 왕복오래달리기 기준 입력
                    if endurance_point >= 85:
                        endurance_point = 1
                        return endurance_point
                    elif endurance_point >= 63 and endurance_point < 85:
                        endurance_point = 2
                        return endurance_point
                    elif endurance_point >= 45 and endurance_point < 63:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 23 and endurance_point < 45:
                        endurance_point = 4
                        return endurance_point
                    else:
                        endurance_point = 5
                        return endurance_point
                    return endurance_point
                if self.grade == 6 and self.gender == "male":
                    # 6학년 남학생 왕복오래달리기 기준 입력
                    if endurance_point >= 104:
                        endurance_point = 1
                        return endurance_point
                    elif endurance_point >= 78 and endurance_point < 104:
                        endurance_point = 2
                        return endurance_point
                    elif endurance_point >= 54 and endurance_point < 78:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 32 and endurance_point < 54:
                        endurance_point = 4
                        return endurance_point
                    else:
                        endurance_point = 5
                        return endurance_point
                    return endurance_point
                if self.grade == 6 and self.gender == "female":
                    # 6학년 여학생 왕복오래달리기 기준 입력
                    if endurance_point >= 93:
                        endurance_point = 1
                        return endurance_point
                    elif endurance_point >= 69 and endurance_point < 93:
                        endurance_point = 2
                        return endurance_point
                    elif endurance_point >= 50 and endurance_point < 69:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 25 and endurance_point < 50:
                        endurance_point = 4
                        return endurance_point
                    else:
                        endurance_point = 5
                        return endurance_point
                    return endurance_point
        elif self.longTimeRun:
            if self.stepTest:
                return "한 종목만 입력하세요"
            else:
                endurance_point = self.longTimeRun
                if self.grade == 5 and self.gender == "male":
                    # 5학년 남학생 오래달리기 기준 입력
                    if endurance_point >= 480:
                        endurance_point = 5
                        return endurance_point
                    elif endurance_point >= 410 and endurance_point < 480:
                        endurance_point = 4
                        return endurance_point
                    elif endurance_point >= 325 and endurance_point < 410:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 282 and endurance_point < 325:
                        endurance_point = 2
                        return endurance_point
                    else:
                        endurance_point = 1
                        return endurance_point
                    return endurance_point
                if self.grade == 5 and self.gender == "female":
                    # 5학년 여학생 오래달리기 기준 입력
                    if endurance_point >= 502:
                        endurance_point = 5
                        return endurance_point
                    elif endurance_point >= 442 and endurance_point < 502:
                        endurance_point = 4
                        return endurance_point
                    elif endurance_point >= 360 and endurance_point < 442:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 300 and endurance_point < 360:
                        endurance_point = 2
                        return endurance_point
                    else:
                        endurance_point = 1
                        return endurance_point
                    return endurance_point
                if self.grade == 6 and self.gender == "male":
                    # 6학년 남학생 오래달리기 기준 입력
                    if endurance_point >= 450:
                        endurance_point = 5
                        return endurance_point
                    elif endurance_point >= 380 and endurance_point < 450:
                        endurance_point = 4
                        return endurance_point
                    elif endurance_point >= 315 and endurance_point < 380:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 251 and endurance_point < 315:
                        endurance_point = 2
                        return endurance_point
                    else:
                        endurance_point = 1
                        return endurance_point
                    return endurance_point
                if self.grade == 6 and self.gender == "female":
                    # 6학년 여학생 오래달리기 기준 입력
                    if endurance_point >= 480:
                        endurance_point = 5
                        return endurance_point
                    elif endurance_point >= 430 and endurance_point < 480:
                        endurance_point = 4
                        return endurance_point
                    elif endurance_point >= 354 and endurance_point < 430:
                        endurance_point = 3
                        return endurance_point
                    elif endurance_point >= 300 and endurance_point < 354:
                        endurance_point = 2
                        return endurance_point
                    else:
                        endurance_point = 1
                        return endurance_point
                    return endurance_point
        else:
            endurance_point = self.stepTest
            if self.grade == 5 and self.gender == "male":
                # 5학년 남학생 스텝검사 기준 입력
                if endurance_point >= 76:
                    endurance_point = 5
                    return endurance_point
                elif endurance_point >= 62 and endurance_point < 76:
                    endurance_point = 4
                    return endurance_point
                elif endurance_point >= 52 and endurance_point < 62:
                    endurance_point = 3
                    return endurance_point
                elif endurance_point >= 47 and endurance_point < 52:
                    endurance_point = 2
                    return endurance_point
                else:
                    endurance_point = 1
                    return endurance_point
                return endurance_point
            if self.grade == 5 and self.gender == "female":
                # 5학년 여학생 스텝검사 기준 입력
                if endurance_point >= 76:
                    endurance_point = 1
                    return endurance_point
                elif endurance_point >= 62 and endurance_point < 76:
                    endurance_point = 2
                    return endurance_point
                elif endurance_point >= 52 and endurance_point < 62:
                    endurance_point = 3
                    return endurance_point
                elif endurance_point >= 47 and endurance_point < 52:
                    endurance_point = 4
                    return endurance_point
                else:
                    endurance_point = 5
                    return endurance_point
                return endurance_point
            if self.grade == 6 and self.gender == "male":
                # 6학년 남학생 스텝검사 기준 입력
                if endurance_point >= 76:
                    endurance_point = 1
                    return endurance_point
                elif endurance_point >= 62 and endurance_point < 76:
                    endurance_point = 2
                    return endurance_point
                elif endurance_point >= 52 and endurance_point < 62:
                    endurance_point = 3
                    return endurance_point
                elif endurance_point >= 47 and endurance_point < 52:
                    endurance_point = 4
                    return endurance_point
                else:
                    endurance_point = 5
                    return endurance_point
                return endurance_point
            if self.grade == 6 and self.gender == "female":
                # 6학년 여학생 스텝검사 기준 입력
                if endurance_point >= 76:
                    endurance_point = 1
                    return endurance_point
                elif endurance_point >= 62 and endurance_point < 76:
                    endurance_point = 2
                    return endurance_point
                elif endurance_point >= 52 and endurance_point < 62:
                    endurance_point = 3
                    return endurance_point
                elif endurance_point >= 47 and endurance_point < 52:
                    endurance_point = 4
                    return endurance_point
                else:
                    endurance_point = 5
                    return endurance_point
                return endurance_point

    def flexibility_point(self):
        if self.bendFoward == None:
            self.bendFoward = 0
            return self.bendFoward

        if self.totalFlexibility == None:
            self.totalFlexibility = 0
            return self.totalFlexibility

        flexibility_point = 0

        if self.bendFoward == 0 and self.totalFlexibility == 0:
            return "측정 결과를 입력하세요"

        if self.bendFoward:
            if self.totalFlexibility:
                return "한 종목만 입력하세요"
            else:
                flexibility_point = self.bendFoward
                if self.grade == 5 and self.gender == "male":
                    # 5학년 남학생 윗몸앞으로굽히기 기준 입력
                    if flexibility_point >= 8:
                        flexibility_point = 1
                        return flexibility_point
                    elif flexibility_point >= 5 and flexibility_point < 8:
                        flexibility_point = 2
                        return flexibility_point
                    elif flexibility_point >= 1 and flexibility_point < 5:
                        flexibility_point = 3
                        return flexibility_point
                    elif flexibility_point >= -4 and flexibility_point < 1:
                        flexibility_point = 4
                        return flexibility_point
                    else:
                        flexibility_point = 5
                        return flexibility_point
                    return flexibility_point
                if self.grade == 5 and self.gender == "female":
                    # 5학년 여학생 윗몸앞으로굽히기 기준 입력
                    if flexibility_point >= 10:
                        flexibility_point = 1
                        return flexibility_point
                    elif flexibility_point >= 7 and flexibility_point < 10:
                        flexibility_point = 2
                        return flexibility_point
                    elif flexibility_point >= 5 and flexibility_point < 7:
                        flexibility_point = 3
                        return flexibility_point
                    elif flexibility_point >= 1 and flexibility_point < 5:
                        flexibility_point = 4
                        return flexibility_point
                    else:
                        flexibility_point = 5
                        return flexibility_point
                    return flexibility_point
                if self.grade == 6 and self.gender == "male":
                    # 6학년 남학생 윗몸앞으로굽히기 기준 입력
                    if flexibility_point >= 8:
                        flexibility_point = 1
                        return flexibility_point
                    elif flexibility_point >= 5 and flexibility_point < 8:
                        flexibility_point = 2
                        return flexibility_point
                    elif flexibility_point >= 1 and flexibility_point < 5:
                        flexibility_point = 3
                        return flexibility_point
                    elif flexibility_point >= -4 and flexibility_point < 1:
                        flexibility_point = 4
                        return flexibility_point
                    else:
                        flexibility_point = 5
                        return flexibility_point
                    return flexibility_point
                if self.grade == 6 and self.gender == "female":
                    # 6학년 여학생 윗몸앞으로굽히기 기준 입력
                    if flexibility_point >= 16:
                        flexibility_point = 1
                        return flexibility_point
                    elif flexibility_point >= 12 and flexibility_point < 16:
                        flexibility_point = 2
                        return flexibility_point
                    elif flexibility_point >= 8 and flexibility_point < 12:
                        flexibility_point = 3
                        return flexibility_point
                    elif flexibility_point >= 4 and flexibility_point < 8:
                        flexibility_point = 4
                        return flexibility_point
                    else:
                        flexibility_point = 5
                        return flexibility_point
                    return flexibility_point
        else:
            flexibility_point = self.totalFlexibility
            # 종합유연성 기준 입력
            if flexibility_point >= 8:
                flexibility_point = 1
                return flexibility_point
            elif flexibility_point >= 7 and flexibility_point < 8:
                flexibility_point = 2
                return flexibility_point
            elif flexibility_point >= 6 and flexibility_point < 7:
                flexibility_point = 3
            elif flexibility_point >= 5 and flexibility_point < 6:
                flexibility_point = 4
                return flexibility_point
            else:
                flexibility_point = 5
                return flexibility_point
            return flexibility_point

    def strength_point(self):

        if self.sitUp == None:
            self.sitUp = 0
            return self.sitUp

        if self.grip == None:
            self.grip = 0
            return self.grip

        strength_point = 0

        if self.sitUp == 0 and self.grip == 0:
            return "측정 결과를 입력하세요"

        if self.sitUp:
            if self.grip:
                return "한 종목만 입력하세요"
            else:
                strength_point = self.sitUp
                if self.gender == "male":
                    # 5,6학년 남학생 윗몸말아올리기 기준
                    if strength_point >= 80:
                        strength_point = 1
                        return strength_point
                    elif strength_point >= 40 and strength_point < 80:
                        strength_point = 2
                        return strength_point
                    elif strength_point >= 22 and strength_point < 40:
                        strength_point = 3
                        return strength_point
                    elif strength_point >= 10 and strength_point < 22:
                        strength_point = 4
                        return strength_point
                    else:
                        strength_point = 5
                        return strength_point
                    return strength_point
                if self.gender == "female":
                    # 5,6학년 여학생 윗몸말아올리기 기준
                    if strength_point >= 60:
                        strength_point = 1
                        return strength_point
                    elif strength_point >= 29 and strength_point < 60:
                        strength_point = 2
                        return strength_point
                    elif strength_point >= 18 and strength_point < 29:
                        strength_point = 3
                        return strength_point
                    elif strength_point >= 6 and strength_point < 18:
                        strength_point = 4
                        return strength_point
                    else:
                        strength_point = 5
                        return strength_point
                    return strength_point
        else:
            strength_point = self.grip
            if self.grade == 5 and self.gender == "male":
                # 5학년 남학생 악력 기준 입력
                if strength_point >= 31:
                    strength_point = 1
                    return strength_point
                elif strength_point >= 23 and strength_point < 31:
                    strength_point = 2
                    return strength_point
                elif strength_point >= 17 and strength_point < 23:
                    strength_point = 3
                    return strength_point
                elif strength_point >= 12.5 and strength_point < 17:
                    strength_point = 4
                    return strength_point
                else:
                    strength_point = 5
                    return strength_point
                return strength_point
            if self.grade == 6 and self.gender == "male":
                # 6학년 남학생 윗몸앞으로굽히기 기준 입력
                if strength_point >= 35:
                    strength_point = 1
                    return strength_point
                elif strength_point >= 26.5 and strength_point < 35:
                    strength_point = 2
                    return strength_point
                elif strength_point >= 19 and strength_point < 26.5:
                    strength_point = 3
                    return strength_point
                elif strength_point >= 15 and strength_point < 19:
                    strength_point = 4
                    return strength_point
                else:
                    strength_point = 5
                    return strength_point
                return strength_point
            if self.grade == 5 and self.gender == "female":
                # 5학년 여학생 윗몸앞으로굽히기 기준 입력
                if strength_point >= 29:
                    strength_point = 1
                    return strength_point
                elif strength_point >= 19 and strength_point < 29:
                    strength_point = 2
                    return strength_point
                elif strength_point >= 15.5 and strength_point < 19:
                    strength_point = 3
                    return strength_point
                elif strength_point >= 12 and strength_point < 15.5:
                    strength_point = 4
                    return strength_point
                else:
                    strength_point = 5
                    return strength_point
                return strength_point
            if self.grade == 6 and self.gender == "female":
                # 6학년 여학생 윗몸앞으로굽히기 기준 입력
                if strength_point >= 33:
                    strength_point = 1
                    return strength_point
                elif strength_point >= 22 and strength_point < 33:
                    strength_point = 2
                    return strength_point
                elif strength_point >= 19 and strength_point < 22:
                    strength_point = 3
                    return strength_point
                elif strength_point >= 14 and strength_point < 19:
                    strength_point = 4
                    return strength_point
                else:
                    strength_point = 5
                    return strength_point
                return strength_point

    def quickness_point(self):

        if self.sprint == None:
            self.sprint = 0
            return self.sprint

        if self.longJump == None:
            self.longJump = 0
            return self.longJump

        quickness_point = 0

        if self.sprint == 0 and self.longJump == 0:
            return "측정 결과를 입력하세요"

        if self.sprint:
            if self.longJump:
                return "한 종목만 입력하세요"
            else:
                quickness_point = self.sprint
                # 5학년 남학생 50m 기준
                if self.grade == 5 and self.gender == "male":
                    if quickness_point >= 13.21:
                        quickness_point = 5
                        return quickness_point
                    elif quickness_point >= 10.21 and quickness_point < 13.21:
                        quickness_point = 4
                        return quickness_point
                    elif quickness_point >= 9.41 and quickness_point < 10.21:
                        quickness_point = 3
                        return quickness_point
                    elif quickness_point >= 8.51 and quickness_point < 9.41:
                        quickness_point = 2
                        return quickness_point
                    else:
                        quickness_point = 1
                        return quickness_point
                    return quickness_point
                # 6학년 남학생 50m 기준 입력
                if self.grade == 6 and self.gender == "male":
                    if quickness_point >= 12.51:
                        quickness_point = 5
                        return quickness_point
                    elif quickness_point >= 10.01 and quickness_point < 12.51:
                        quickness_point = 4
                        return quickness_point
                    elif quickness_point >= 9.11 and quickness_point < 10.01:
                        quickness_point = 3
                        return quickness_point
                    elif quickness_point >= 8.11 and quickness_point < 9.11:
                        quickness_point = 2
                        return quickness_point
                    else:
                        quickness_point = 1
                        return quickness_point
                    return quickness_point
                # 5학년 여학생 50m 기준 입력
                if self.grade == 5 and self.gender == "female":
                    if quickness_point >= 13.01:
                        quickness_point = 5
                        return quickness_point
                    elif quickness_point >= 10.71 and quickness_point < 13.01:
                        quickness_point = 4
                        return quickness_point
                    elif quickness_point >= 9.91 and quickness_point < 10.71:
                        quickness_point = 3
                        return quickness_point
                    elif quickness_point >= 8.91 and quickness_point < 9.91:
                        quickness_point = 2
                        return quickness_point
                    else:
                        quickness_point = 1
                        return quickness_point
                    return quickness_point
                # 6학년 여학생 50m 기준 입력
                if self.grade == 6 and self.gender == "female":
                    if quickness_point >= 12.91:
                        quickness_point = 5
                        return quickness_point
                    elif quickness_point >= 10.71 and quickness_point < 12.91:
                        quickness_point = 4
                        return quickness_point
                    elif quickness_point >= 9.81 and quickness_point < 10.71:
                        quickness_point = 3
                        return quickness_point
                    elif quickness_point >= 8.91 and quickness_point < 9.81:
                        quickness_point = 2
                        return quickness_point
                    else:
                        quickness_point = 1
                        return quickness_point
                    return quickness_point

        else:
            quickness_point = self.longJump
            # 5학년 남학생 제자리멀리뛰기 기준
            if self.grade == 5 and self.gender == "male":
                if quickness_point >= 180.1:
                    quickness_point = 1
                    return quickness_point
                elif quickness_point >= 159.1 and quickness_point < 180.1:
                    quickness_point = 2
                    return quickness_point
                elif quickness_point >= 141.1 and quickness_point < 159.1:
                    quickness_point = 3
                    return quickness_point
                elif quickness_point >= 111.1 and quickness_point < 141.1:
                    quickness_point = 4
                    return quickness_point
                else:
                    quickness_point = 5
                    return quickness_point
                return quickness_point
            # 6학년 남학생 제자리멀리뛰기 기준 입력
            if self.grade == 6 and self.gender == "male":
                if quickness_point >= 200.1:
                    quickness_point = 1
                    return quickness_point
                elif quickness_point >= 167.1 and quickness_point < 200.1:
                    quickness_point = 2
                    return quickness_point
                elif quickness_point >= 148.1 and quickness_point < 167.1:
                    quickness_point = 3
                    return quickness_point
                elif quickness_point >= 122.1 and quickness_point < 148.1:
                    quickness_point = 4
                    return quickness_point
                else:
                    quickness_point = 5
                    return quickness_point
                return quickness_point
            # 5학년 여학생 제자리멀리뛰기 기준 입력
            if self.grade == 5 and self.gender == "female":
                if quickness_point >= 170.1:
                    quickness_point = 1
                    return quickness_point
                elif quickness_point >= 139.1 and quickness_point < 170.1:
                    quickness_point = 2
                    return quickness_point
                elif quickness_point >= 123.1 and quickness_point < 139.1:
                    quickness_point = 3
                    return quickness_point
                elif quickness_point >= 100.1 and quickness_point < 123.1:
                    quickness_point = 4
                    return quickness_point
                else:
                    quickness_point = 5
                    return quickness_point
                return quickness_point
            # 6학년 여학생 제자리멀리뛰기 기준 입력
            if self.grade == 6 and self.gender == "female":
                if quickness_point >= 175.1:
                    quickness_point = 1
                    return quickness_point
                elif quickness_point >= 144.1 and quickness_point < 175.1:
                    quickness_point = 2
                    return quickness_point
                elif quickness_point >= 127.1 and quickness_point < 144.1:
                    quickness_point = 3
                    return quickness_point
                elif quickness_point >= 100.1 and quickness_point < 127.1:
                    quickness_point = 4
                    return quickness_point
                else:
                    quickness_point = 5
                    return quickness_point
                return quickness_point

    def bmi(self):
        return round(self.weight / ((self.height / 100) ** 2), 2)

    def fat_point(self):
        fat_point = 0
        bmi = 0

        if self.height and self.weight:
            bmi = round(self.weight / ((self.height / 100) ** 2), 2)
            fat_point = bmi
            # 5학년 남학생 bmi 기준
            if self.grade == 5 and self.gender == "male":
                if fat_point >= 30:
                    fat_point = "고도비만"
                    return fat_point
                elif fat_point >= 24.5 and fat_point < 30:
                    fat_point = "경도비만"
                    return fat_point
                elif fat_point >= 21.7 and fat_point < 24.5:
                    fat_point = "과체중"
                    return fat_point
                elif fat_point >= 14.6 and fat_point < 21.7:
                    fat_point = "정상"
                    return fat_point
                else:
                    fat_point = "마름"
                    return fat_point
                return fat_point
            # 6학년 남학생 bmi 기준
            if self.grade == 6 and self.gender == "male":
                if fat_point >= 30:
                    fat_point = "고도비만"
                    return fat_point
                elif fat_point >= 25 and fat_point < 30:
                    fat_point = "경도비만"
                    return fat_point
                elif fat_point >= 22.6 and fat_point < 25:
                    fat_point = "과체중"
                    return fat_point
                elif fat_point >= 14.9 and fat_point < 22.6:
                    fat_point = "정상"
                    return fat_point
                else:
                    fat_point = "마름"
                    return fat_point
                return fat_point
            # 5학년 여학생 bmi 기준
            if self.grade == 5 and self.gender == "female":
                if fat_point >= 30:
                    fat_point = "고도비만"
                    return fat_point
                elif fat_point >= 23.1 and fat_point < 30:
                    fat_point = "경도비만"
                    return fat_point
                elif fat_point >= 20.7 and fat_point < 23.1:
                    fat_point = "과체중"
                    return fat_point
                elif fat_point >= 14.3 and fat_point < 20.7:
                    fat_point = "정상"
                    return fat_point
                else:
                    fat_point = "마름"
                    return fat_point
                return fat_point
            # 6학년 여학생 bmi 기준
            if self.grade == 6 and self.gender == "female":
                if fat_point >= 30:
                    fat_point = "고도비만"
                    return fat_point
                elif fat_point >= 24 and fat_point < 30:
                    fat_point = "경도비만"
                    return fat_point
                elif fat_point >= 21.5 and fat_point < 24:
                    fat_point = "과체중"
                    return fat_point
                elif fat_point >= 14.7 and fat_point < 21.5:
                    fat_point = "정상"
                    return fat_point
                else:
                    fat_point = "마름"
                    return fat_point
                return fat_point
        elif self.height != 0 and self.weight == 0:
            return "몸무게를 입력하세요"
        elif self.weight != 0 and self.height == 0:
            return "키를 입력하세요"
        else:
            return "키/몸무게를 입력하세요"

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "Verify AI Trainer Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
