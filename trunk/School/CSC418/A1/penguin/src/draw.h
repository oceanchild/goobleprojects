/*
 * draw.h
 *
 *  Created on: Oct 9, 2012
 *      Author: g9sk
 */

#ifndef DRAW_H_
#define DRAW_H_

#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include <GL/glui.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// ------------ REQUIRED DATA STRUCTURES --------------------
typedef struct{
	float x;
	float y;
} Point;

const float DEG2RAD = 3.14159 / 180;
// Joint parameters
const float JOINT_MIN = -45.0f;
const float JOINT_MAX =  45.0f;
const int BEAK_MIN = 0;
const int BEAK_MAX = 6;
extern float leg1Rotation;
extern float leg2Rotation;
extern float armRotation;
extern float foot1Rotation;
extern float foot2Rotation;
extern float headRotation;
extern int beakDistance;

const float LEG_OFFSET_X = 0.2f;
const float LEG_OFFSET_Y = -0.5;

const float LEG_SCALE = 0.3f;

const float FOOT_OFFSET_X = -0.5f;
const float FOOT_OFFSET_Y = -0.4f;

const float FOOT_WIDTH_REL_TO_LEG = 2.0f;
const float FOOT_LENGTH_REL_TO_LEG = 0.33f;

const double LEG_ROTATION_SPEED = 0.1;
const int BEAK_SEPARATION_SPEED = 1;

void drawPolygon(int n, Point points[]);
void drawSquare(float width);
void drawCircle(float radius);
void drawHead();
void drawBeak();
void drawArm();
void drawLeg(float leftOrRight, float legRotation, float footRotation);

#endif /* DRAW_H_ */