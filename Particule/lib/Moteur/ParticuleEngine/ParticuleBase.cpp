#include "ParticuleBase.hpp"

Vector2::Vector2() {
    this->x = 0;
    this->y = 0;
}
Vector2::Vector2(float x, float y) {
    this->x = x;
    this->y = y;
};
void Vector2::Set(float x, float y) {
    this->x = x;
    this->y = y;
};
void Vector2::Set(Vector2* vect) {
    this->x = vect->x;
    this->y = vect->y;
};

void Vector2::Set(Vector2 vect) {
    this->x = vect.x;
    this->y = vect.y;
};

void Vector2::Add(Vector2* vect) {
    this->x += vect->x;
    this->y += vect->y;
};
void Vector2::Add(float x, float y) {
    this->x += x;
    this->y += y;
};

bool Vector2::operator==(const Vector2& other) {
    return this->x == other.x && this->y == other.y;
}

bool Vector2::operator!=(const Vector2& other) {
    return !(this->x == other.x && this->y == other.y);
}

Vector2 Vector2::operator+(const Vector2& other) {
    return Vector2(this->x + other.x, this->y + other.y);
}

Vector2 Vector2::operator-(const Vector2& other) {
    return Vector2(this->x - other.x, this->y - other.y);
}

Vector2 Vector2::operator*(const Vector2& other) {
    return Vector2(this->x * other.x, this->y * other.y);
}

Vector2 Vector2::operator/(const Vector2& other) {
    return Vector2(this->x / other.x, this->y / other.y);
}



Object::Object(const char* name, const char* UUID) {
    this->name = (unsigned char*)name;
    this->ID = (unsigned char*)UUID;
};


unsigned char* Object::GetInstanceID() {
    return ID;
};
unsigned char* Object::ToString() {
    return name;
};


// Overload operator
bool Object::operator==(const Object& obj) {
    return this->ID == obj.ID;
}

bool Object::operator!=(const Object& obj) {
    return this->ID != obj.ID;
}