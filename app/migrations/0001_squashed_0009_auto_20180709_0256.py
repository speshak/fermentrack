# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-04-16 15:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_allow_null_device_beer_links'), ('app', '0003_prep for serial udev'), ('app', '0004_update udev to add blank'), ('app', '0005_Add Profile Type'), ('app', '0006_auto_20171021_1344'), ('app', '0007_auto_20171105_1523'), ('app', '0008_auto_20180429_2322'), ('app', '0009_auto_20180709_0256')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeerLogPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beer_temp', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('beer_set', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('beer_ann', models.CharField(max_length=255, null=True)),
                ('fridge_temp', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('fridge_set', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('fridge_ann', models.CharField(max_length=255, null=True)),
                ('room_temp', models.DecimalField(decimal_places=10, max_digits=13, null=True)),
                ('state', models.IntegerField(choices=[(0, 'IDLE'), (1, 'STATE_OFF'), (2, 'DOOR_OPEN'), (3, 'HEATING'), (4, 'COOLING'), (5, 'WAITING_TO_COOL'), (6, 'WAITING_TO_HEAT'), (7, 'WAITING_FOR_PEAK_DETECT'), (8, 'COOLING_MIN_TIME'), (9, 'HEATING_MIN_TIME')], default=0)),
                ('log_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('temp_format', models.CharField(choices=[('C', 'Celsius'), ('F', 'Fahrenheit')], default='C', max_length=1)),
            ],
            options={
                'ordering': ['log_time'],
                'verbose_name': 'Beer Log Point',
                'managed': False,
                'verbose_name_plural': 'Beer Log Points',
            },
        ),
        migrations.CreateModel(
            name='PinDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=16)),
                ('type', models.CharField(default='', max_length=8)),
                ('pin', models.IntegerField(default=-1)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SensorDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=16)),
                ('device_index', models.IntegerField(default=-1)),
                ('type', models.IntegerField(default=0)),
                ('chamber', models.IntegerField(default=0)),
                ('beer', models.IntegerField(default=0)),
                ('device_function', models.IntegerField(choices=[(0, 'NONE'), (1, 'Chamber Door'), (2, 'Heating Relay'), (3, 'Cooling Relay'), (4, 'Chamber Light'), (5, 'Chamber Temp'), (6, 'Room (outside) Temp'), (7, 'Chamber Fan'), (9, 'Beer Temp')], default=0)),
                ('hardware', models.IntegerField(choices=[(0, 'NONE'), (1, 'PIN'), (2, 'ONEWIRE_TEMP'), (3, 'ONEWIRE_2413'), (4, 'ONEWIRE_2408/Valve')], default=2)),
                ('deactivated', models.IntegerField(default=0)),
                ('pin', models.IntegerField(default=0)),
                ('calibrate_adjust', models.FloatField(default=0.0)),
                ('pio', models.IntegerField(default=None, null=True)),
                ('invert', models.IntegerField(choices=[(0, 'Not Inverted'), (1, 'Inverted')], default=1)),
            ],
            options={
                'verbose_name': 'Sensor Device',
                'managed': False,
                'verbose_name_plural': 'Sensor Devices',
            },
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('format', models.CharField(default='F', max_length=1)),
                ('model_version', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='BrewPiDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(help_text='Unique name for this device', max_length=48, unique=True)),
                ('temp_format', models.CharField(choices=[('C', 'Celsius'), ('F', 'Fahrenheit')], default='C', help_text='Temperature units', max_length=1)),
                ('data_point_log_interval', models.IntegerField(choices=[(10, '10 Seconds'), (30, '30 Seconds'), (60, '1 Minute'), (120, '2 Minutes'), (300, '5 Minutes'), (600, '10 Minutes'), (1800, '30 Minutes'), (3600, '1 Hour')], default=30, help_text='Time between logged data points')),
                ('useInetSocket', models.BooleanField(default=False, help_text='Whether or not to use an internet socket (rather than local)')),
                ('socketPort', models.IntegerField(default=2222, help_text='The internet socket to use (only used if useInetSocket above is "True")', validators=[django.core.validators.MinValueValidator(10, 'Port must be 10 or higher'), django.core.validators.MaxValueValidator(65535, 'Port must be 65535 or lower')])),
                ('socketHost', models.CharField(default='localhost', help_text='The interface to bind for the internet socket (only used if useInetSocket above is "True")', max_length=128)),
                ('logging_status', models.CharField(choices=[('active', 'Active'), ('paused', 'Paused'), ('stopped', 'Stopped')], default='stopped', help_text='Data logging status', max_length=10)),
                ('serial_port', models.CharField(default='auto', help_text='Serial port to which the BrewPi device is connected', max_length=255)),
                ('serial_alt_port', models.CharField(default='None', help_text='Alternate serial port to which the BrewPi device is connected (??)', max_length=255)),
                ('board_type', models.CharField(choices=[('uno', 'Arduino Uno (or compatible)'), ('esp8266', 'ESP8266'), ('leonardo', 'Arduino Leonardo'), ('core', 'Core'), ('photon', 'Photon')], default='uno', help_text='Board type to which BrewPi is connected', max_length=10)),
                ('status', models.CharField(choices=[('active', 'Active, Managed by Circus'), ('unmanaged', 'Active, NOT managed by Circus'), ('disabled', 'Explicitly disabled, cannot be launched'), ('updating', 'Disabled, pending an update')], default='active', max_length=15)),
                ('socket_name', models.CharField(default='BEERSOCKET', help_text='Name of the file-based socket (Only used if useInetSocket is False)', max_length=25)),
                ('connection_type', models.CharField(choices=[('serial', 'Serial (Arduino and others)'), ('wifi', 'WiFi (ESP8266)')], default='serial', help_text='Type of connection between the Raspberry Pi and the hardware', max_length=15)),
                ('wifi_host', models.CharField(default='None', help_text='mDNS host name or IP address for WiFi connected hardware (only used if connection_type is wifi)', max_length=40)),
                ('wifi_port', models.IntegerField(default=23, help_text='The internet socket to use (only used if connection_type is wifi)', validators=[django.core.validators.MinValueValidator(10, 'Port must be 10 or higher'), django.core.validators.MaxValueValidator(65535, 'Port must be 65535 or lower')])),
                ('time_profile_started', models.DateTimeField(blank=True, default=None, null=True)),
                ('active_beer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Beer')),
            ],
            options={
                'verbose_name': 'BrewPi Device',
                'verbose_name_plural': 'BrewPi Devices',
            },
        ),
        migrations.CreateModel(
            name='FermentationProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Pending Delete')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='FermentationProfilePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttl', models.DurationField(help_text='Time at which we should arrive at this temperature')),
                ('temperature_setting', models.DecimalField(decimal_places=2, help_text='The temperature the beer should be when TTL has passed', max_digits=5, null=True)),
                ('temp_format', models.CharField(default='F', max_length=1)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.FermentationProfile')),
            ],
        ),
        migrations.CreateModel(
            name='NewControlConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempFormat', models.CharField(default='C', max_length=1)),
                ('heater1_kp', models.FloatField(help_text='Actuator output in % = Kp * input error')),
                ('heater1_ti', models.IntegerField()),
                ('heater1_td', models.IntegerField()),
                ('heater1_infilt', models.IntegerField()),
                ('heater1_dfilt', models.IntegerField()),
                ('heater2_kp', models.FloatField()),
                ('heater2_ti', models.IntegerField()),
                ('heater2_td', models.IntegerField()),
                ('heater2_infilt', models.IntegerField()),
                ('heater2_dfilt', models.IntegerField()),
                ('cooler_kp', models.FloatField()),
                ('cooler_ti', models.IntegerField()),
                ('cooler_td', models.IntegerField()),
                ('cooler_infilt', models.IntegerField()),
                ('cooler_dfilt', models.IntegerField()),
                ('beer2fridge_kp', models.FloatField()),
                ('beer2fridge_ti', models.IntegerField()),
                ('beer2fridge_td', models.IntegerField()),
                ('beer2fridge_infilt', models.IntegerField()),
                ('beer2fridge_dfilt', models.IntegerField()),
                ('beer2fridge_pidMax', models.FloatField()),
                ('minCoolTime', models.IntegerField()),
                ('minCoolIdleTime', models.IntegerField()),
                ('heater1PwmPeriod', models.IntegerField()),
                ('heater2PwmPeriod', models.IntegerField()),
                ('coolerPwmPeriod', models.IntegerField()),
                ('mutexDeadTime', models.IntegerField()),
                ('preset_name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OldControlConstants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempSetMin', models.FloatField(help_text="The fridge and beer temperatures cannot go below this value. Units are specified by 'Temperature format' below.", verbose_name='Min Temperature')),
                ('tempSetMax', models.FloatField(help_text="The fridge and beer temperatures cannot go above this value. Units are specified by 'Temperature format' below.", verbose_name='Max Temperature')),
                ('Kp', models.FloatField(help_text='The beer temperature error is multiplied by Kp to give the proportional of the PID value', verbose_name='PID: Kp')),
                ('Ki', models.FloatField(help_text='When the integral is active, the error is added to the integral every 30 sec. The result is multiplied by Ki to give the integral part.', verbose_name='PID: Ki')),
                ('Kd', models.FloatField(help_text='The derivative of the beer temperature is multiplied by Kd to give the derivative part of the PID value', verbose_name='PID: Kd')),
                ('pidMax', models.FloatField(help_text='Defines the maximum difference between the beer temp setting and fridge temp setting. The fridge setting will be clipped to this range.', verbose_name='PID: maximum')),
                ('iMaxErr', models.FloatField(help_text='The integral is only active when the temperature is close to the target temperature. This is the maximum error for which the integral is active.', verbose_name='Integrator: Max temp error C')),
                ('idleRangeH', models.FloatField(help_text='When the fridge temperature is within this range, it will not heat or cool, regardless of other settings', verbose_name='Temperature idle range top')),
                ('idleRangeL', models.FloatField(help_text='When the fridge temperature is within this range, it will not heat or cool, regardless of other settings', verbose_name='Temperature idle range bottom')),
                ('heatTargetH', models.FloatField(help_text='When the overshoot lands under this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Heating target upper bound')),
                ('heatTargetL', models.FloatField(help_text='When the overshoot lands above this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Heating target lower bound')),
                ('coolTargetH', models.FloatField(help_text='When the overshoot lands under this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Cooling target upper bound')),
                ('coolTargetL', models.FloatField(help_text='When the overshoot lands above this value, the peak is within the target range and the estimator is not adjusted', verbose_name='Cooling target lower bound')),
                ('maxHeatTimeForEst', models.IntegerField(help_text='The time the fridge has been heating is used to estimate overshoot. This is the maximum time that is taken into account.', verbose_name='Maximum time in seconds for heating overshoot estimator')),
                ('maxCoolTimeForEst', models.IntegerField(help_text='Maximum time the fridge has been cooling is used to estimate overshoot. This is the maximum time that is taken into account.', verbose_name='Maximum time in seconds for cooling overshoot estimator')),
                ('beerFastFilt', models.IntegerField(help_text='The beer fast filter is used for display and data logging. More filtering gives a smoother line but also more delay.', verbose_name='Beer fast filter delay time')),
                ('beerSlowFilt', models.IntegerField(help_text='The beer slow filter is used for the control algorithm. The fridge temperature setting is calculated from this filter. Because a small difference in beer temperature cases a large adjustment in the fridge temperature, more smoothing is needed.', verbose_name='Beer slow filter delay time')),
                ('beerSlopeFilt', models.IntegerField(help_text='The slope is calculated every 30 sec and fed to this filter. More filtering means a smoother fridge setting.', verbose_name='Beer slope filter delay time')),
                ('fridgeFastFilt', models.IntegerField(help_text='The fridge fast filter is used for on-off control, display, and logging. It needs to have a small delay.', verbose_name='Fridge fast filter delay time')),
                ('fridgeSlowFilt', models.IntegerField(help_text='The fridge slow filter is used for peak detection to adjust the overshoot estimators. More smoothing is needed to prevent small fluctuations from being recognized as peaks.', verbose_name='Fridge slow filter delay time')),
                ('fridgeSlopeFilt', models.IntegerField(help_text='Fridge slope filter is not used in this revision of the firmware.', verbose_name='Fridge slope filter delay time')),
                ('lah', models.IntegerField(choices=[(1, 'YES'), (0, 'No')], default=0, help_text='If set to yes the chamber light (if assigned a pin) will be used in place of the heat pin', verbose_name='Using light as heater?')),
                ('hs', models.IntegerField(choices=[(1, 'YES'), (0, 'No')], default=0, help_text='If this option is set to yes, the rotary encoder will use half steps', verbose_name='Use half steps for rotary encoder?')),
                ('tempFormat', models.CharField(choices=[('F', 'Fahrenheit'), ('C', 'Celsius')], default='F', help_text='This is the temperature format that will be used by the device', max_length=1, verbose_name='Temperature format')),
                ('preset_name', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='active_profile',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.FermentationProfile'),
        ),
        migrations.AddField(
            model_name='beer',
            name='device',
            field=models.ForeignKey(help_text='The linked temperature control device from which data is logged', null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.BrewPiDevice'),
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='prefer_connecting_via_udev',
            field=models.BooleanField(default=True, help_text='Prefer to connect to the device with the correct serial number instead of the serial_port'),
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='udev_serial_number',
            field=models.CharField(blank=True, default='', help_text='USB Serial ID number for autodetection of serial port', max_length=255),
        ),
        migrations.AddField(
            model_name='brewpidevice',
            name='wifi_host_ip',
            field=models.CharField(default='', help_text='Cached IP address in case of mDNS issues (only used if connection_type is wifi)', max_length=46),
        ),
        migrations.AddField(
            model_name='fermentationprofile',
            name='profile_type',
            field=models.CharField(default='Standard Profile', help_text='Type of temperature profile', max_length=32),
        ),
        migrations.AddField(
            model_name='beer',
            name='gravity_enabled',
            field=models.BooleanField(default=False, help_text='Is gravity logging enabled for this beer log?'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='When the beer log was initially created'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='format',
            field=models.CharField(default='F', help_text='Temperature format to write the logs in', max_length=1),
        ),
        migrations.AlterField(
            model_name='beer',
            name='model_version',
            field=models.IntegerField(default=1, help_text='Version # used for the logged file format'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(db_index=True, help_text='Name of the beer being logged (must be unique)', max_length=255),
        ),
        migrations.AlterField(
            model_name='brewpidevice',
            name='active_beer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Beer'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='model_version',
            field=models.IntegerField(default=2, help_text='Version # used for the logged file format'),
        ),
    ]
