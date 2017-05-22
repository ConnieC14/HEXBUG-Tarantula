

//************************** GLOBAL VARIABLES *******************************//
//***************************************************************************//
/********* INITIALIZE GROUND AND POWER PINS  ***********/
#define PIN_GROUND A1 
#define PIN_VSOURCE A0 // BLUE

/*************** INITIALIZE BUTTON PINS  ***************/
/// MOVE FORWARD
#define TURN_RIGHT A2
#define TURN_LEFT A4
// MOVE BACKWARDS
#define TURN_LEFT_BACK A3
#define TURN_RIGHT_BACK A5
int commands[] = {1, 2, 3, 4};

//************************** SERIAL PORT INIT *******************************//
//***************************************************************************//
unsigned long lastCommand_millis = 0;
int commndDuration_millis = 520;
int serialBaudRate = 9600;


//**************************** INIT FUNCTIONS ******************************//
//***************************************************************************//
void setup() { 
  Serial.begin(serialBaudRate);

  // print help
  Serial.println("TestHexBugController: starting...");
  Serial.println("Commands Include: ");
  Serial.println("    'W' = Forward");
  Serial.println("    'A' = Turn CC");
  Serial.println("    'D' = Turn C");
  Serial.println("    'S' = Back");

  // put your setup code here, to run once:
  pinMode(PIN_GROUND, OUTPUT); digitalWrite(PIN_GROUND, LOW);
  pinMode(PIN_VSOURCE, OUTPUT); digitalWrite(PIN_VSOURCE, HIGH);
 
  stop();
}

void stop() {
  pinMode(A2, INPUT);
  digitalWrite(A2, LOW);
  pinMode(A3, INPUT);
  digitalWrite(A3, LOW);
  pinMode(A4, INPUT);
  digitalWrite(A4, LOW);
  pinMode(A5, INPUT);
  digitalWrite(A5, LOW);
}


void move_forward() {
  pinMode(TURN_RIGHT, OUTPUT);
  digitalWrite(TURN_RIGHT, LOW);
  pinMode(TURN_LEFT, OUTPUT);
  digitalWrite(TURN_LEFT, LOW);
}

void move_backward() {
  pinMode(TURN_RIGHT_BACK, OUTPUT);
  digitalWrite(TURN_RIGHT_BACK, LOW);
  pinMode(TURN_LEFT_BACK, OUTPUT);
  digitalWrite(TURN_LEFT_BACK, LOW);
}

void turn_clock() {
  pinMode(TURN_RIGHT_BACK, OUTPUT);
  digitalWrite(TURN_RIGHT_BACK, LOW);
  pinMode(TURN_RIGHT, OUTPUT);
  digitalWrite(TURN_RIGHT, LOW);
}

void turn_cclock() {
  pinMode(TURN_LEFT_BACK, OUTPUT);
  digitalWrite(TURN_LEFT_BACK, LOW);
  pinMode(TURN_LEFT, OUTPUT);
  digitalWrite(TURN_LEFT, LOW);
}


//**************************** IMPLEMENTATION ******************************//
//***************************************************************************//
void loop() {
  // print the string when a newline arrives:
  if (millis() > lastCommand_millis + commndDuration_millis) {
    lastCommand_millis = millis() + 500; //don't do this branch for a while
    stop();
  }
}


//****************************** SERIAL READ *******************************//
//***************************************************************************//
void issueCommand(int command_pin_ind) {
  stop();
  switch (command_pin_ind) {
    case 1:
      Serial.println("MOVING FORWARD");
      move_forward();
      lastCommand_millis = millis();  //time the command was received
      break;
    case 2:
      Serial.println("TURNING CC");
      turn_cclock();
      lastCommand_millis = millis();  //time the command was received
      break;
    case 3:
      Serial.println("TURNING CLOCK");
      turn_clock();
      lastCommand_millis = millis();  //time the command was received
      break;
    case 4:
      Serial.println("MOVING BACKWARD");
      move_backward();
      lastCommand_millis = millis();  //time the command was received
    default:
      // if nothing else matches, do the default
      // default is optional
      break;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
  hardware serial RX.  This routine is run between each
  time loop() runs, so using delay inside loop can delay
  response.  Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    Serial.print("Command: "); Serial.println(inChar);
    switch (inChar) {
      case 'W':
        issueCommand(commands[0]); break;
      case 'A':
        issueCommand(commands[1]); break;
      case 'D':
        issueCommand(commands[2]); break;
      case 'S':
        issueCommand(commands[3]); break;
    }
  }
}

