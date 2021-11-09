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

PlayerController::PlayerController(GameObject* gameObject, Texture* Bas1, Texture* Bas2,
    Texture* Bas3, Texture* Haut1, Texture* Haut2, Texture* Haut3, Texture* Droite1,
    Texture* Droite2, Texture* Droite3, Texture* Gauche1, Texture* Gauche2, Texture* Gauche3,
    int Vitesse, const char* UUID) : MonoBehaviour("PlayerController", gameObject, UUID) {
    this->Bas1 = Bas1;
    this->Bas2 = Bas2;
    this->Bas3 = Bas3;
    this->Haut1 = Haut1;
    this->Haut2 = Haut2;
    this->Haut3 = Haut3;
    this->Droite1 = Droite1;
    this->Droite2 = Droite2;
    this->Droite3 = Droite3;
    this->Gauche1 = Gauche1;
    this->Gauche2 = Gauche2;
    this->Gauche3 = Gauche3;
    this->Vitesse = Vitesse;
    this->Frame = 0;

};

void PlayerController::Update() {
    return;
    ML_rectangle((127 / 2) - (12 / 2), (63 / 2) - (20 / 2), (127 / 2) + (12 / 2), (63 / 2) - (20 / 2) + 20, 0, ML_WHITE, ML_WHITE);
    if (IsKeyDown(KEY_CTRL_UP)) {
        this->gameObject->transform->position->y += ((0) - (this->Vitesse));
        if (((((this->Frame) == (0))) || (((this->Frame) == (2))))) {
            ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Haut1;

        }
        else {
            if (((this->Frame) == (1))) {
                ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Haut2;

            }
            else {
                ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Haut3;

            }

        }

    }
    else {
        if (IsKeyDown(KEY_CTRL_DOWN)) {
            this->gameObject->transform->position->y += this->Vitesse;
            if (((((this->Frame) == (0))) || (((this->Frame) == (2))))) {
                ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Bas1;

            }
            else {
                if (((this->Frame) == (1))) {
                    ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Bas2;

                }
                else {
                    ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Bas3;

                }

            }

        }
        else {
            if (IsKeyDown(KEY_CTRL_RIGHT)) {
                this->gameObject->transform->position->x += this->Vitesse;
                if (((((this->Frame) == (0))) || (((this->Frame) == (2))))) {
                    ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Droite1;

                }
                else {
                    if (((this->Frame) == (1))) {
                        ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Droite2;

                    }
                    else {
                        ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Droite3;

                    }

                }

            }
            else {
                if (IsKeyDown(KEY_CTRL_LEFT)) {
                    this->gameObject->transform->position->x += ((0) - (this->Vitesse));
                    if (((((this->Frame) == (0))) || (((this->Frame) == (2))))) {
                        ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Gauche1;

                    }
                    else {
                        if (((this->Frame) == (1))) {
                            ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Gauche2;

                        }
                        else {
                            ((Sprite*)this->gameObject->GetComponent("Sprite"))->image = this->Gauche3;

                        }

                    }

                }

            }

        }

    }
    this->Frame = mod((int)((this->Frame) + (1)), (int)4);
    gameObject->scene->AllCameras[0]->gameObject->transform->position->Set(*gameObject->transform->position - *(new Vector2(127 / 2, 63 / 2)) + *(new Vector2(16 / 2, 20 / 2)));

}
void PlayerController::Start() {
    this->Frame = 0;

}



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


Scene* SceneManager::GetSceneInBuild(int index) {
    Scene* newScene = new Scene();
    newScene->sceneManager = this;

    Texture* Texture_UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c = new Texture("Texture", 16, 20, UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c);
    Texture* Texture_UUID_3b28f421_9575_4c12_91c4_2c145b435538 = new Texture("Texture", 16, 20, UUID_3b28f421_9575_4c12_91c4_2c145b435538);
    Texture* Texture_UUID_53848287_45f6_410e_b7f2_b01019c5a1e9 = new Texture("Texture", 16, 20, UUID_53848287_45f6_410e_b7f2_b01019c5a1e9);
    Texture* Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af = new Texture("Texture", 16, 20, UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af);
    Texture* Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea = new Texture("Texture", 16, 20, UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea);
    Texture* Texture_UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae = new Texture("Texture", 16, 20, UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae);
    Texture* Texture_UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b = new Texture("Texture", 16, 20, UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b);
    Texture* Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6 = new Texture("Texture", 16, 20, UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6);
    Texture* Texture_UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f = new Texture("Texture", 16, 20, UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f);
    Texture* Texture_UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f = new Texture("Texture", 16, 20, UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f);
    Texture* Texture_UUID_e870f483_8f84_44ae_b86c_bb1978372306 = new Texture("Texture", 16, 20, UUID_e870f483_8f84_44ae_b86c_bb1978372306);
    Texture* Texture_UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6 = new Texture("Texture", 16, 20, UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6);
    if (index == 0) {
        GameObject* UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46;
        GameObject* UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca;
        GameObject* UUID_400c4826_db9d_4390_963a_d132c010b431;
        Sprite* UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3;
        PlayerController* UUID_6640de22_b0db_4537_8522_f3a7a703d68f;

        Tilemap* UUID_fbe0964f_80f0_4bb3_9701_3928fd378215;

        Camera* UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4;

        UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46 = new GameObject(newScene, "Camera", "UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46");
        UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->activeSelf = true;
        UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->activeInHierarchy = true;
        UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->isStatic = false;
        UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->transform->position->Set(0, 0);
        UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->transform->localPosition->Set(0, 0);
        newScene->AddGameObject(UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46);
        UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca = new GameObject(newScene, "Tilemap", "UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca");
        UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->activeSelf = true;
        UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->activeInHierarchy = true;
        UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->isStatic = false;
        UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->transform->position->Set(0, 0);
        UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->transform->localPosition->Set(0, 0);
        newScene->AddGameObject(UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca);
        UUID_400c4826_db9d_4390_963a_d132c010b431 = new GameObject(newScene, "Player", "UUID_400c4826_db9d_4390_963a_d132c010b431");
        UUID_400c4826_db9d_4390_963a_d132c010b431->activeSelf = true;
        UUID_400c4826_db9d_4390_963a_d132c010b431->activeInHierarchy = true;
        UUID_400c4826_db9d_4390_963a_d132c010b431->isStatic = false;
        UUID_400c4826_db9d_4390_963a_d132c010b431->transform->position->Set(40.0, 20.0);
        UUID_400c4826_db9d_4390_963a_d132c010b431->transform->localPosition->Set(40.0, 20.0);
        newScene->AddGameObject(UUID_400c4826_db9d_4390_963a_d132c010b431);




        UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4 = new Camera(UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46, "UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4");
        UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->AddComponent((Component*)UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4);





        UUID_fbe0964f_80f0_4bb3_9701_3928fd378215 = new Tilemap(UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca, new Vector2(10, 10), new Vector2(16, 16), "UUID_fbe0964f_80f0_4bb3_9701_3928fd378215");
        UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->AddComponent((Component*)UUID_fbe0964f_80f0_4bb3_9701_3928fd378215);
        static int UUID_fbe0964f_80f0_4bb3_9701_3928fd378215_TilemapDatas[] = { 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
        UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->Datas = UUID_fbe0964f_80f0_4bb3_9701_3928fd378215_TilemapDatas;
        UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images = new Texture * [2];
        UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[0] = new Texture();
        UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[1] = Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af;





        UUID_6640de22_b0db_4537_8522_f3a7a703d68f = new PlayerController(UUID_400c4826_db9d_4390_963a_d132c010b431, Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea, Texture_UUID_53848287_45f6_410e_b7f2_b01019c5a1e9, Texture_UUID_3b28f421_9575_4c12_91c4_2c145b435538, Texture_UUID_e870f483_8f84_44ae_b86c_bb1978372306, Texture_UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c, Texture_UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae, Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af, Texture_UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6, Texture_UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f, Texture_UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f, Texture_UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b, Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6, 5, "UUID_6640de22_b0db_4537_8522_f3a7a703d68f");
        UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_6640de22_b0db_4537_8522_f3a7a703d68f);


        UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3 = new Sprite(UUID_400c4826_db9d_4390_963a_d132c010b431, Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea, "UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3");
        UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3);


    }

    return newScene;

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
