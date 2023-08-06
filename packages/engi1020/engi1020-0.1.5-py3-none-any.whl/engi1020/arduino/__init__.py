"""Arduino API wrapper.

This code assumes that there is only one Arduino device connected.
"""

import click
import nanpy


# Assuming there's only one Arduino connected to this computer, here it is.
a = None

def arduino():
    """Return Arduino API, instantiating if needed."""

    global a

    if a is None:
        a = nanpy.ArduinoApi(connection=nanpy.SerialManager())

    return a


def analogRead(pin):
    return arduino().analogRead(pin+14)

def analogWrite(pin):
    return arduino().analogWrite(pin+14)

def digitalRead(pin):
    return arduino().digitalRead(pin)

def digitalWrite(pin):
    return arduino().digitalWrite(pin)


@click.group()
def cli():
    pass

@cli.group()
def analog():
    """Commands to interact with analog pins."""
    pass

@analog.command('read')
@click.argument('pin', type=int)
def analog_read(pin):
    """Read a value from an analog pin."""
    print(analogRead(pin))

@cli.group()
def digital():
    """Commands to interact with digital pins."""
    pass

@digital.command('read')
@click.argument('pin', type=int)
def digital_read(pin):
    """Read a value from a digital pin."""
    print(digitalRead(pin))


lcd_instance = None

def get_lcd():
    global lcd_instance

    if lcd_instance is None:
        from . import rgb_lcd
        lcd_instance = rgb_lcd.rgb_lcd(arduino().connection)
        lcd_instance.setRGB(255, 255, 255)

    return lcd_instance


@cli.group()
def lcd():
    """Commands to interact with an RGB LCD screen."""

@lcd.command()
@click.argument('message')
def print(message):
    get_lcd().printString(message)

@lcd.command()
@click.argument('red', type=int)
@click.argument('green', type=int)
@click.argument('blue', type=int)
def rgb(red, green, blue):
    get_lcd().setRGB(red, green, blue)
