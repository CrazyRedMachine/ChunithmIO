#include <Keyboard.h>
#include <FastLED.h>
#define LEFT_PIN      5
#define RIGHT_PIN     6
#define NUM_LEDS    3

CRGB left_leds[NUM_LEDS];
CRGB right_leds[NUM_LEDS];

void setup() {
 Keyboard.begin();
 FastLED.addLeds<WS2811, LEFT_PIN, RGB>(left_leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
 FastLED.addLeds<WS2811, RIGHT_PIN, RGB>(right_leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
 FastLED.setBrightness(64);
 delay(1000);
 fill_solid(left_leds, NUM_LEDS, CRGB(0x7F,0,0x23));
 fill_solid(right_leds, NUM_LEDS, CRGB(0x7F,0,0x23));
 FastLED.show(); 
 pinMode(8, INPUT_PULLUP);
 pinMode(9, INPUT_PULLUP);
 pinMode(10, INPUT_PULLUP);
 pinMode(11, INPUT_PULLUP);
 pinMode(12, INPUT_PULLUP);
 pinMode(13, INPUT_PULLUP);
 delay(1000);
}

void loop() {
  if (digitalRead(8) == HIGH)
  {
    Keyboard.press('a');
  }
  else
  {
    Keyboard.release('a');
  }
  if (digitalRead(11) == HIGH)
  {
    Keyboard.press('b');
  }
  else
  {
    Keyboard.release('b');
  }
  if (digitalRead(9) == HIGH)
   {
    Keyboard.press('c');
  }
  else
  {
    Keyboard.release('c');
  }
  if (digitalRead(12) == HIGH)
  {
    Keyboard.press('d');
  }
  else
  {
    Keyboard.release('d');
  }
  if (digitalRead(10) == HIGH)
  {
    Keyboard.press('e');
  }
  else
  {
    Keyboard.release('e');
  }
  if (digitalRead(13) == HIGH)
  {
    Keyboard.press('f');
  }
  else
  {
    Keyboard.release('f');
  }  
}
