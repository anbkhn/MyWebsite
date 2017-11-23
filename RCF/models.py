from django.db import models

class Relay(models.Model):
    relay_name = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=200)
    def __str__(self):
        return self.relay_name + "-"+ self.vendor_name

class CTVT(models.Model):
    ctvt_des = models.CharField(max_length=500)
    ctvt_code = models.CharField(max_length=1)
    def __str__(self):
        return self.ctvt_des +" " +  self.ctvt_code

class Frq(models.Model):
    frq_des = models.CharField(max_length=10)
    frq_code = models.CharField(max_length=1)
    def __str__(self):
        return self.frq_des + " " + self.frq_code


class CurrentRating(models.Model):
    cur_des = models.CharField(max_length=10)
    cur_code = models.CharField(max_length=1)
    def __str__(self):
        return self.cur_des + " " + self.cur_code


class Power(models.Model):
    power_des = models.CharField(max_length=100)
    power_code = models.CharField(max_length=1)
    def __str__(self):
        return self.power_des + " " + self.power_code


class Outline(models.Model):
    outline_des = models.CharField(max_length=500)
    outline_code = models.CharField(max_length=1)
    def __str__(self):
        return self.outline_des + " " + self.outline_des


class InOut_1(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code

class InOut_2(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code

class InOut_3(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code

class InOut_4(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code

class InOut_5(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code

class InOut_6(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code

class InOut_7(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code

class InOut_8(models.Model):
    inout_des = models.CharField(max_length=500)
    inout_code = models.CharField(max_length=2)
    inout_config = models.CharField(max_length=100)
    def __str__(self):
        return self.inout_des + "-" + self.inout_config + " " + self.inout_code



class Com_Port(models.Model):
    comport_des = models.CharField(max_length=500)
    comport_code = models.CharField(max_length=2)
    def __str__(self):
        return self.comport_des + " " + self.comport_code


class Function(models.Model):
    function_des = models.CharField(max_length=500)
    function_code = models.CharField(max_length=2)
    def __str__(self):
        return self.function_des + " " + self.function_code


class Protocol(models.Model):
    protocol_des = models.CharField(max_length=500)
    protocol_code = models.CharField(max_length=1)
    def __str__(self):
        return self.protocol_des + " " + self.protocol_code


class Language(models.Model):
    lang_des = models.CharField(max_length=100)
    lang_code = models.CharField(max_length=1)
    def __str__(self):
        return self.lang_des + " " + self.lang_code
