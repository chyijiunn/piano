from picozero import Speaker
import machine ,utime
speaker = Speaker(21)
button0  = machine.Pin(  0 , machine.Pin.IN, machine.Pin.PULL_UP)
button1  = machine.Pin(  1 , machine.Pin.IN, machine.Pin.PULL_UP)
button2  = machine.Pin(  2 , machine.Pin.IN, machine.Pin.PULL_UP)
button3  = machine.Pin(  3 , machine.Pin.IN, machine.Pin.PULL_UP)
button4  = machine.Pin(  4 , machine.Pin.IN, machine.Pin.PULL_UP)
button5  = machine.Pin(  5 , machine.Pin.IN, machine.Pin.PULL_UP)
button6  = machine.Pin(  6 , machine.Pin.IN, machine.Pin.PULL_UP)
button7  = machine.Pin(  7 , machine.Pin.IN, machine.Pin.PULL_UP)
button8  = machine.Pin(  8 , machine.Pin.IN, machine.Pin.PULL_UP)
button9  = machine.Pin(  9 , machine.Pin.IN, machine.Pin.PULL_UP)
button10  = machine.Pin(  10 , machine.Pin.IN, machine.Pin.PULL_UP)
button11  = machine.Pin(  11 , machine.Pin.IN, machine.Pin.PULL_UP)
button12  = machine.Pin(  12 , machine.Pin.IN, machine.Pin.PULL_UP)
button13  = machine.Pin(  13 , machine.Pin.IN, machine.Pin.PULL_UP)
button14  = machine.Pin(  14 , machine.Pin.IN, machine.Pin.PULL_UP)
button15  = machine.Pin(  15 , machine.Pin.IN, machine.Pin.PULL_UP)
button16  = machine.Pin(  16 , machine.Pin.IN, machine.Pin.PULL_UP)
button17  = machine.Pin(  17 , machine.Pin.IN, machine.Pin.PULL_UP)
button18  = machine.Pin(  18 , machine.Pin.IN, machine.Pin.PULL_UP)
button19  = machine.Pin(  19 , machine.Pin.IN, machine.Pin.PULL_UP)
button20  = machine.Pin(  20 , machine.Pin.IN, machine.Pin.PULL_UP)
button21  = machine.Pin(  21 , machine.Pin.IN, machine.Pin.PULL_UP)
button22  = machine.Pin(  22 , machine.Pin.IN, machine.Pin.PULL_UP)
button23  = machine.Pin(  23 , machine.Pin.IN, machine.Pin.PULL_UP)
button24  = machine.Pin(  24 , machine.Pin.IN, machine.Pin.PULL_UP)
button26  = machine.Pin(  26 , machine.Pin.IN, machine.Pin.PULL_UP)
button27  = machine.Pin(  27 , machine.Pin.IN, machine.Pin.PULL_UP)


tempo = 0.1 

while True:
    if button1.value() == 0:speaker.play('d3',tempo)
    if button2.value() == 0:speaker.play('e3',tempo)
    if button3.value() == 0:speaker.play('f3',tempo)
    if button4.value() == 0:speaker.play('g3',tempo)
    if button5.value() == 0:speaker.play('a3',tempo)
    if button6.value() == 0:speaker.play('b3',tempo)
    if button7.value() == 0:speaker.play('c4',tempo)
    if button8.value() == 0:speaker.play('d4',tempo)
    if button9.value() == 0:speaker.play('e4',tempo)
    if button10.value() == 0:speaker.play('f4',tempo)
    if button11.value() == 0:speaker.play('g4',tempo)
    if button12.value() == 0:speaker.play('a4',tempo)
    if button13.value() == 0:speaker.play('b4',tempo)
    if button14.value() == 0:speaker.play('c5',tempo)
    if button15.value() == 0:speaker.play('d5',tempo)
    if button16.value() == 0:speaker.play('e5',tempo)
    if button17.value() == 0:speaker.play('f5',tempo)
    if button18.value() == 0:speaker.play('g5',tempo)
    if button19.value() == 0:speaker.play('a5',tempo)
    if button20.value() == 0:speaker.play('b5',tempo)
    if button21.value() == 0:speaker.play('c6',tempo)
    if button22.value() == 0:speaker.play('d6',tempo)
    if button23.value() == 0:speaker.play('e6',tempo)
    if button24.value() == 0:speaker.play('f6',tempo)
    #if button25.value() == 0:speaker.play('g6',tempo)
    if button26.value() == 0:speaker.play('a6',tempo)
    if button27.value() == 0:speaker.play('b6',tempo)
    speaker.off()