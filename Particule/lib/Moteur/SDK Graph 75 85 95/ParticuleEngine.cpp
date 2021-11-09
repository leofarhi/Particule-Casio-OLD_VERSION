extern "C"
{
#include "keybios.h"
#include "fxlib.h"
#include <stdio.h>
#include "stdio.h"
#include "stdlib.h"

#include "string.h"
#include "time.h"
}
#include "Announcement.h"
#include "MonochromeLib.h"
#include "List.h"
#include <iostream>
#include <math.h>
#include "usefull.h"
#include "Ressources.h"
#include "ParticuleEngine.hpp"

int LenChar(char* txt) {
    return strlen(txt);
}

int mod(int x, int m) {
    return (x % m + m) % m;
}

enum Tag
{
    Untagged = 0,
    Respawn = 1,
    Finish = 2,
    EditorOnly = 3,
    MainCamera = 4,
    Player = 5,
    GameController = 6
};

enum Layer
{
    Default = 0,
    TransparentFX = 1,
    IgnoreRaycast = 2,
    Water = 3,
    UI = 4
};

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
void Vector2::Set(Vector2 vect) {
    this->x = vect.x;
    this->y = vect.y;
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

Component::Component(const char* name, GameObject* gameObject, const char* UUID) : Object(name, UUID)
{
    this->gameObject = gameObject;
};

Component::~Component() {
    delete tag;
}


Transform::Transform(GameObject* gameObject, const char* UUID, const char* name) : Component(name, gameObject, UUID) {
    childCount = 0;
    //eulerAngles = new Vector2();
    //forward = None
    hasChanged = NULL;
    hierarchyCapacity = NULL;
    hierarchyCount = NULL;
    //localEulerAngles = new Vector2();
    localPosition = new Vector2();
    //localRotation = NULL;
    localScale = new Vector2(1, 1);
    //localToWorldMatrix = NULL;
    lossyScale = new Vector2(1, 1);
    parent = NULL;
    //children = []
    position = new Vector2();
    //self.right = None
    root = NULL;
    //rotation = NULL;
    //self.up = None
    //worldToLocalMatrix = NULL;
    lastPosition = new Vector2();
};

Transform::~Transform() {
    //delete localRotation;
    //delete localToWorldMatrix;
    delete parent;
    delete root;
    //delete rotation;
    //delete worldToLocalMatrix;
}

void Transform::SetParent(Transform* transform) {
    if (parent != NULL) {
        parent->children.Remove(this);
    }
    transform->children.Add(this);
    parent = transform;
}

void Transform::Start() {
    lastPosition->x = position->x;
    lastPosition->y = position->y;
}

void Transform::Update() {
    childCount = children.Count;

    if (parent == NULL) {

        if (*position != *localPosition) {
            if (*localPosition != *lastPosition) {
                position->x = localPosition->x;
                position->y = localPosition->y;
            }
        }
        localPosition->x = position->x;
        localPosition->y = position->y;
    }
    else
    {
        //return;
        if ((*position != *lastPosition) && (*position == (*localPosition + *parent->position))) {
            localPosition->Set(*localPosition + (*lastPosition - *position));
        }
        position->Set(*localPosition + *parent->position);

    }
    lastPosition->x = position->x;
    lastPosition->y = position->y;
}


Behaviour::Behaviour(const char* name, GameObject* gameObject, const char* UUID) : Component(name, gameObject, UUID) {
    enabled = true;
    isActiveAndEnabled = true;
};

/*
enum ScaleMode
{
    //https://docs.unity3d.com/ScriptReference/ScaleMode.html
    StretchToFill,
    ScaleAndCrop,
    ScaleToFit,
};
class CallbackEventHandler{
    //https://docs.unity3d.com/ScriptReference/UIElements.CallbackEventHandler.html

};

class Focusable : public CallbackEventHandler {
    //https://docs.unity3d.com/ScriptReference/UIElements.Focusable.html

};

class VisualElement : public Focusable {
    //https://docs.unity3d.com/ScriptReference/UIElements.VisualElement.html

};
*/


enum TextureDimension
{
    Unknown,
    None,
    Any,
    Tex2D,
    Tex3D,
    Cube,
    Tex2DArray,
    CubeArray
};

enum FilterMode
{
    Point,
    Bilinear,
    Trilinear
};

Texture::Texture() : Object("None", NULL) {
    textureData = "";
    this->width = 0;
    this->height = 0;
};
Texture::Texture(const char* name, int width, int height, const unsigned char* Data, const char* UUID) : Object(name, UUID) {
    textureData = (unsigned char*)Data;
    this->width = width;
    this->height = height;
};

MonoBehaviour::MonoBehaviour(const char* name, GameObject* gameObject, const char* UUID) : Behaviour(name, gameObject, UUID) {
    useGUILayout = true;
};


GameObject::GameObject(Scene* scene, const char* name, const char* UUID) : Object(name, UUID)
{
    this->scene = scene;
    this->transform = new Transform(this);
    activeInHierarchy = true;
    activeSelf = true;
    isStatic = false;
    layer = Default;
    sceneCullingMask = NULL;
    tag = Untagged;
    //ListOfComponent.Add(transform);
};

GameObject::~GameObject() {
    delete transform;
}

bool GameObject::IsActive() {
    if (!activeSelf) {
        activeInHierarchy = false;
        return false;
    }
    if (transform->parent != NULL) {
        if (!transform->parent->gameObject->activeInHierarchy || !transform->parent->gameObject->activeSelf) {
            activeInHierarchy = false;
            return false;
        }
    }
    activeInHierarchy = true;
    return true;
}

void GameObject::Update() {
    this->transform->Update();
    if (!IsActive()) {
        return;
    }
    for (int i = 0; i < ListOfComponent.Count; i++)
    {
        ListOfComponent[i]->Update();
    }
};

void GameObject::Start() {
    this->transform->Start();
    if (!IsActive()) {
        return;
    }
    for (int i = 0; i < ListOfComponent.Count; i++)
    {
        ListOfComponent[i]->Start();
    }
};

void GameObject::AddComponent(Component* component) {
    ListOfComponent.Add(component);
};
Component* GameObject::GetComponent(const char* name) {
    for (int i = 0; i < ListOfComponent.Count; i++)
    {
        if (ListOfComponent[i]->name == (unsigned char*)name)
            return ListOfComponent[i];
    }
    return NULL;
};


GameObject* GameObject::Find(unsigned char* name) {
    return FindWithName(name, this);
};


void Scene::AddGameObject(GameObject* gObj) {
    AllGameObject.Add(gObj);
};

void Scene::Update() {
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        AllGameObject[i]->Update();
    }
};

void Scene::Start() {
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        AllGameObject[i]->Start();
    }
};

Camera::Camera(GameObject* gameObject, const char* UUID) : Behaviour("Camera", gameObject, UUID) {
    gameObject->scene->AllCameras.Add(this);
}

Image::Image(GameObject* gameObject, Texture* image, const char* UUID) : MonoBehaviour("Image", gameObject, UUID) {
    this->image = image;
};

void Image::Update() {
    float posX = gameObject->transform->position->x;
    float posY = gameObject->transform->position->y;
    float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
    float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
    if (posX - camX + image->height > 0 && posX - camX < 128 && posY - camY + image->height>0 && posY - camY < 64)
        ML_bmp_or_cl((const unsigned char*)image->textureData, (int)(posX - camX), (int)(posY - camY), image->width, image->height);
};

Sprite::Sprite(GameObject* gameObject, Texture* image, const char* UUID) : MonoBehaviour("Sprite", gameObject, UUID) {
    this->image = image;
};

void Sprite::Update() {
    float posX = gameObject->transform->position->x;
    float posY = gameObject->transform->position->y;
    float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
    float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
    if (posX - camX + image->height > 0 && posX - camX < 128 && posY - camY + image->height>0 && posY - camY < 64)
        ML_bmp_or_cl((const unsigned char*)image->textureData, (int)(posX - camX), (int)(posY - camY), image->width, image->height);
};


Rigidbody::Rigidbody(GameObject* gameObject, float Mass, bool UseGravity, bool IsKinematic, const char* UUID) : MonoBehaviour("Rigidbody", gameObject, UUID) {
    this->Mass = Mass;
    this->UseGravity = UseGravity;
    this->IsKinematic = IsKinematic;
    this->velocity = new Vector2();

};

Rigidbody::~Rigidbody() {
    delete velocity;
}

void Rigidbody::Start() {
    this->velocity->Set(0, 0);
}


Text::Text(GameObject* gameObject, unsigned char* text, const char* UUID) : MonoBehaviour("Text", gameObject, UUID) {
    this->text = text;

};

void Text::Update() {
    float posX = gameObject->transform->position->x;
    float posY = gameObject->transform->position->y;
    float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
    float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
    PrintMini((int)(posX - camX), (int)(posY - camY), (unsigned char*)this->text, MINI_OVER);
}

Tilemap::Tilemap(GameObject* gameObject, Vector2* sizeTilemap, Vector2* sizeCase, const char* UUID) : MonoBehaviour("Tilemap", gameObject, UUID) {
    this->sizeTilemap = sizeTilemap;
    this->sizeCase = sizeCase;
};

Tilemap::~Tilemap() {
    delete[] images;
    delete[] Datas;
}

void Tilemap::Update() {
    float posX = gameObject->transform->position->x;
    float posY = gameObject->transform->position->y;
    float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
    float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
    for (int h = 0; h < sizeTilemap->y; h++) {
        int x = 0;
        for (int w = h * sizeTilemap->x; w < (h + 1) * sizeTilemap->x; w++) {
            int tempx = (int)((posX - camX) + x * sizeCase->x);
            int tempy = (int)((posY - camY) + h * sizeCase->y);
            if (tempx + sizeCase->x > 0 && tempx < 128 && tempy + sizeCase->y>0 && tempy < 64)
                ML_bmp_or_cl((const unsigned char*)(images[Datas[w]])->textureData, tempx, tempy, (images[Datas[w]])->width, (images[Datas[w]])->height);
            x++;
        }
    }

};




void SceneManager::LoadScene(int index) {
    AllSceneLoaded.Clear();
    AllSceneLoaded.Add(GetSceneInBuild(index));
};
void SceneManager::LoadScene(unsigned char* name) {
    AllSceneLoaded.Clear();
    AllSceneLoaded.Add(GetSceneInBuild(name));
};

GameObject* SceneManager::FindWithName(unsigned char* name) {
    for (int i = 0; i < AllSceneLoaded.Count; i++)
    {
        for (int o = 0; o < AllSceneLoaded[i]->AllGameObject.Count; o++) {
            if (AllSceneLoaded[i]->AllGameObject[o]->name == name) {
                return AllSceneLoaded[i]->AllGameObject[o];
            }
        }
    }
    return NULL;
}


void SceneManager::UpdateScene() {
    for (int i = 0; i < AllSceneLoaded.Count; i++)
    {
        AllSceneLoaded[i]->Update();
    }
};

void SceneManager::StartScene() {
    for (int i = 0; i < AllSceneLoaded.Count; i++)
    {
        AllSceneLoaded[i]->Start();
    }
}

Scene* SceneManager::GetSceneInBuild(unsigned char* name) {
    unsigned char* AllName[] = { "Main" };
    int count = 0;
    for (int i = 0; i < count; i++)
    {
        if (name == AllName[i]) {
            return GetSceneInBuild(i);
        }
    }
    return NULL;
}


void LoadScene(Scene* scene, int nb) {
    scene->sceneManager->LoadScene(nb);
    scene->sceneManager->StartScene();
};

GameObject* FindWithName(unsigned char* name, GameObject* gameObject) {
    return gameObject->scene->sceneManager->FindWithName(name);
};
