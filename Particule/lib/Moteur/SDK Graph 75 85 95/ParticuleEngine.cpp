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

int Random(int start, int end) {
    return (getTicks() % (end - start)) + start;
}

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

Component::Component(const char* name, GameObject* gameObject, const char* UUID) : Object(name, UUID)
{
    this->gameObject = gameObject;
};



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
    //localScale = new Vector2(1, 1);
    //localToWorldMatrix = NULL;
    lossyScale = new Vector2(1, 1);
    parent = NULL;
    //children = []
    position = new Vector2();
    //self.right = None
    //root = NULL;
    //rotation = NULL;
    //self.up = None
    //worldToLocalMatrix = NULL;
    lastPosition = new Vector2();
};


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
    ListOfComponent.Add(transform);
};

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
        if (AllGameObject[i]->IsActive()) {
            for (int o = 0; o < AllGameObject[i]->ListOfComponent.Count; o++)
            {
                AllGameObject[i]->ListOfComponent[o]->PhysicsCalculator();
            }
        }
    }
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        if (AllGameObject[i]->IsActive()) {
            for (int o = 0; o < AllGameObject[i]->ListOfComponent.Count; o++)
            {
                AllGameObject[i]->ListOfComponent[o]->FixedUpdate();
            }
        }
    }
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        if (AllGameObject[i]->IsActive()) {
            for (int o = 0; o < AllGameObject[i]->ListOfComponent.Count; o++)
            {
                AllGameObject[i]->ListOfComponent[o]->Update();
            }
        }
    }
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        if (AllGameObject[i]->IsActive()) {
            for (int o = 0; o < AllGameObject[i]->ListOfComponent.Count; o++)
            {
                AllGameObject[i]->ListOfComponent[o]->LateUpdate();
            }
        }
    }
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        if (AllGameObject[i]->IsActive()) {
            AllGameObject[i]->transform->Update();
        }
    }
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        if (AllGameObject[i]->IsActive()) {
            for (int o = 0; o < AllGameObject[i]->ListOfComponent.Count; o++)
            {
                AllGameObject[i]->ListOfComponent[o]->OnRenderObject();
            }
        }
    }
};

void Scene::Start() {
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        if (AllGameObject[i]->IsActive()) {
            for (int o = 0; o < AllGameObject[i]->ListOfComponent.Count; o++)
            {
                AllGameObject[i]->ListOfComponent[o]->Start();
            }
        }
    }
    for (int i = 0; i < AllGameObject.Count; i++)
    {
        if (AllGameObject[i]->IsActive()) {
            for (int o = 0; o < AllGameObject[i]->ListOfComponent.Count; o++)
            {
                AllGameObject[i]->ListOfComponent[o]->Awake();
            }
        }
    }
};

Camera::Camera(GameObject* gameObject, const char* UUID) : Behaviour("Camera", gameObject, UUID) {
    gameObject->scene->AllCameras.Add(this);
}

Image::Image(GameObject* gameObject, Texture* image, const char* UUID) : MonoBehaviour("Image", gameObject, UUID) {
    this->image = image;
};

void Image::OnRenderObject() {
    float posX = gameObject->transform->position->x;
    float posY = gameObject->transform->position->y;
    float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
    float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
    if (posX - camX + image->height > 0 && posX - camX < 128 && posY - camY + image->height>0 && posY - camY < 64)
        ML_bmp_or_cl((const unsigned char*)image->textureData, (int)(posX - camX), (int)(posY - camY), image->width, image->height);
};

Sprite::Sprite(GameObject* gameObject, Texture* image,bool HaveBackground, const char* UUID) : MonoBehaviour("Sprite", gameObject, UUID) {
    this->image = image;
    this->HaveBackground = HaveBackground;
};

void Sprite::OnRenderObject() {
    float posX = gameObject->transform->position->x;
    float posY = gameObject->transform->position->y;
    float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
    float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
    if (posX - camX + image->height > 0 && posX - camX < 128 && posY - camY + image->height>0 && posY - camY < 64)
        if (HaveBackground)
            ML_rectangle((int)(posX - camX), (int)(posY - camY), (int)(posX - camX)+image->width, (int)(posY - camY)+image->height, 0, ML_WHITE, ML_WHITE);
        ML_bmp_or_cl((const unsigned char*)image->textureData, (int)(posX - camX), (int)(posY - camY), image->width, image->height);
};



Rigidbody::Rigidbody(GameObject* gameObject, float Mass, bool UseGravity, bool IsKinematic, const char* UUID) : MonoBehaviour("Rigidbody", gameObject, UUID) {
    this->Mass = Mass;
    this->UseGravity = UseGravity;
    this->IsKinematic = IsKinematic;
    this->velocity = new Vector2();
    this->lastPosition = new Vector2();

};

void Rigidbody::Start() {
    this->velocity->Set(0, 0);
    this->lastPosition->Set(this->gameObject->transform->position);
    this->MyCollider = (Collider2D*)(((BoxCollider2D*)this->gameObject->GetComponent("BoxCollider2D")));
}


bool Rigidbody::CheckCollider() {
    if (MyCollider != NULL && gameObject->isStatic && !MyCollider->IsTrigger)
        return false;
    for (int i = 0; i < gameObject->scene->LstColliders.Count; i++) {
        if (MyCollider != gameObject->scene->LstColliders[i] && ((Component*)gameObject->scene->LstColliders[i])->gameObject->IsActive()) {
            if (!gameObject->scene->LstColliders[i]->IsTrigger && MyCollider->AreTheyTouching(gameObject->scene->LstColliders[i]))
                return true;
        }
    }
    return false;
}

bool Rigidbody::IsVisible() {
    
    float posX = gameObject->transform->position->x;
    float posY = gameObject->transform->position->y;
    float camX = gameObject->scene->AllCameras[0]->gameObject->transform->position->x;
    float camY = gameObject->scene->AllCameras[0]->gameObject->transform->position->y;
    return (posX - camX + (127 * 2) > 0 && posX - camX < (128 * 2) && posY - camY + (63 * 2)>0 && posY - camY < (64 * 2));
}

void Rigidbody::PhysicsCalculator() {
    if (!(UseGravity && IsVisible()))
        return;

    if (CheckCollider()) {
        gameObject->transform->position->Set(lastPosition);
    }
    else {
        this->velocity->Set(this->velocity->x - (this->gameObject->scene->sceneManager->projectSettings->Gravity->x * this->Mass),
            this->velocity->y - (this->gameObject->scene->sceneManager->projectSettings->Gravity->y * this->Mass));
        this->lastPosition->Set(this->gameObject->transform->position);
    }
    gameObject->transform->position->Add(this->velocity->x, -this->velocity->y);
    if (CheckCollider()) {
        int x = 0;
        int y = 0;
        this->velocity->Set(velocity->x * 2, velocity->y * 2);
        while (y < abs((int)this->velocity->y) || x < abs((int)this->velocity->x))
        {
            if (CheckCollider()) {
                if (y < abs((int)this->velocity->y))
                    gameObject->transform->position->Add(0, -(abs(this->velocity->y) / this->velocity->y) * (-1));
                if (x < abs((int)this->velocity->x))
                    gameObject->transform->position->Add((abs(this->velocity->x) / this->velocity->x) * (-1), 0);
            }
            y++;
            x++;
        }
        this->velocity->Set(0, 0);
    }
    if (CheckCollider()) {
        gameObject->transform->position->Set(lastPosition);
    }
    this->lastPosition->Set(this->gameObject->transform->position);
};

void Rigidbody::LateUpdate() {
    if (CheckCollider()) {
        gameObject->transform->position->Set(lastPosition);
    }

};

void Collider2D::Update() {

    if (gameObject->isStatic && !IsTrigger)
        return;
    for (int i = 0; i < gameObject->scene->LstColliders.Count; i++) {
        if (this != gameObject->scene->LstColliders[i] && gameObject->scene->LstColliders[i]->gameObject->IsActive()) {


            if (AreTheyTouching(gameObject->scene->LstColliders[i])) {
                // collision détectée !
                if (Contains(gameObject->scene->LstColliders[i])) {
                    for (int o = 0; o < gameObject->ListOfComponent.Count; o++) {
                        if (gameObject->scene->LstColliders[i]->IsTrigger || IsTrigger)
                            gameObject->ListOfComponent[o]->OnTriggerStay2D(gameObject->scene->LstColliders[i]);
                        gameObject->ListOfComponent[o]->OnCollisionStay2D(gameObject->scene->LstColliders[i]);
                    }
                }
                else
                {
                    LstColliders.Add(gameObject->scene->LstColliders[i]);
                    for (int o = 0; o < gameObject->ListOfComponent.Count; o++) {
                        if (gameObject->scene->LstColliders[i]->IsTrigger || IsTrigger)
                            gameObject->ListOfComponent[o]->OnTriggerEnter2D(gameObject->scene->LstColliders[i]);
                        gameObject->ListOfComponent[o]->OnCollisionEnter2D(gameObject->scene->LstColliders[i]);
                    }
                }

            }
            else
            {
                if (Contains(gameObject->scene->LstColliders[i])) {
                    for (int o = 0; o < gameObject->ListOfComponent.Count; o++) {
                        if (gameObject->scene->LstColliders[i]->IsTrigger || IsTrigger)
                            gameObject->ListOfComponent[o]->OnTriggerExit2D(gameObject->scene->LstColliders[i]);
                        gameObject->ListOfComponent[o]->OnCollisionExit2D(gameObject->scene->LstColliders[i]);
                    }
                    for (int o = 0; o < LstColliders.Count; o++) {
                        if (LstColliders[o] == gameObject->scene->LstColliders[i]) {
                            LstColliders.RemoveAt(o);
                        }
                    }

                    //LstColliders.Remove(gameObject->scene->LstColliders[i]);
                }
            }
        }
    }
};


BoxCollider2D::BoxCollider2D(GameObject* gameObject, bool IsTrigger, Vector2* center, Vector2* size, const char* UUID) : Collider2D(gameObject, IsTrigger, UUID) {
    ((Object*)this)->name = "BoxCollider2D";
    this->center = center;
    this->size = size;
    //LstColliders.DeleteAct = false;
};

bool BoxCollider2D::AreTheyTouching(Collider2D* collider) {
    int x1 = ((Component*)collider)->gameObject->transform->position->x +
        ((BoxCollider2D*)collider)->center->x - (((BoxCollider2D*)collider)->size->x / 2);
    int x2 = ((Component*)collider)->gameObject->transform->position->x +
        ((BoxCollider2D*)collider)->center->x + (((BoxCollider2D*)collider)->size->x / 2);
    int y1 = ((Component*)collider)->gameObject->transform->position->y +
        ((BoxCollider2D*)collider)->center->y - (((BoxCollider2D*)collider)->size->y / 2);
    int y2 = ((Component*)collider)->gameObject->transform->position->y +
        ((BoxCollider2D*)collider)->center->y + (((BoxCollider2D*)collider)->size->y / 2);
    
    int MyX1 = ((Component*)this)->gameObject->transform->position->x + ((BoxCollider2D*)this)->center->x - (size->x / 2);
    int MyX2 = ((Component*)this)->gameObject->transform->position->x + ((BoxCollider2D*)this)->center->x + (size->x / 2);
    int MyY1 = ((Component*)this)->gameObject->transform->position->y + ((BoxCollider2D*)this)->center->y - (size->y / 2);
    int MyY2 = ((Component*)this)->gameObject->transform->position->y + ((BoxCollider2D*)this)->center->y + (size->y / 2);
    return (x1 < MyX2&&
        x2 > MyX1 &&
        y1 < MyY2&&
        y2 > MyY1);
}




Text::Text(GameObject* gameObject, unsigned char* text, const char* UUID) : MonoBehaviour("Text", gameObject, UUID) {
    this->text = text;

};

void Text::OnRenderObject() {
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


void Tilemap::OnRenderObject() {
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
    for (int i = 0; i < AllSceneLoaded.Count; i++) {
        delete AllSceneLoaded.Pop();
    }
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
    if (LoadSceneAfter > -1) {
        this->LoadScene(LoadSceneAfter);
        this->StartScene();
        LoadSceneAfter = -1;
        return;
    }
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


void LoadScene(Scene* scene, int nb) {
    scene->sceneManager->LoadSceneAfter = nb;
    //scene->sceneManager->LoadScene(nb);
    //scene->sceneManager->StartScene();
};

GameObject* FindWithName(unsigned char* name, GameObject* gameObject) {
    return gameObject->scene->sceneManager->FindWithName(name);
};
