#pragma once

#ifndef ClassParticuleBase
#define ClassParticuleBase
extern "C"
{

#include <stdio.h>
#include "stdio.h"
#include "stdlib.h"

}
class Vector2 {
    //https://docs.unity3d.com/ScriptReference/Vector2.html
public:
    float x;
    float y;
    Vector2();
    Vector2(float x, float y);
    void Set(float x, float y);
    void Set(Vector2* vect);
    void Set(Vector2 vect);
    void Add(float x, float y);
    void Add(Vector2* vect);

    bool operator==(const Vector2& other);

    bool operator!=(const Vector2& other);

    Vector2 operator+(const Vector2& other);

    Vector2 operator-(const Vector2& other);

    Vector2 operator*(const Vector2& other);

    Vector2 operator/(const Vector2& other);
};
/*
class Quaternion {
    //https://docs.unity3d.com/ScriptReference/Quaternion.html
public:

};

class Matrix4x4 {
    //https://docs.unity3d.com/ScriptReference/Matrix4x4.html
public:

};*/

class Object {
    //https://docs.unity3d.com/ScriptReference/Object.html
public:
    Object(const char* name, const char* UUID = NULL);

    virtual ~Object() {};
    //hideFlags c'est pour l'éditeur donc il n'est pas présent
    unsigned char* name;
    unsigned char* GetInstanceID();
    unsigned char* ToString();

    virtual void Destroy() {}
    /*virtual void DestroyImmediate() {}
    virtual void DontDestroyOnLoad() {}
    virtual void FindObjectOfType() {}
    virtual void FindObjectsOfType() {}
    virtual void Instantiate() {}*/

    // Overload operator
    bool operator==(const Object& obj);

    bool operator!=(const Object& obj);
private:
    unsigned char* ID;
};

#endif