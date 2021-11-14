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
    this->lastPosition->Set(gameObject->transform->position->x, gameObject->transform->position->y);
    this->MyBoxCollider = ((BoxCollider2D*)this->gameObject->GetComponent("BoxCollider2D"));
}

void Rigidbody::PhysicsCalculator() {
    //calcule de physique (gravite)
    //a faire
    this->velocity->Set(0, 0);///////////
    this->lastPosition->Set(gameObject->transform->position->x, gameObject->transform->position->y);
};

void Rigidbody::OnCollisionEnter2D(BoxCollider2D* boxCollider2D) {

    if (!(boxCollider2D->IsTrigger || (MyBoxCollider != NULL && MyBoxCollider->IsTrigger)))
        this->velocity->Set(lastPosition->x - gameObject->transform->position->x, lastPosition->y - gameObject->transform->position->y);
}
void Rigidbody::OnCollisionStay2D(BoxCollider2D* boxCollider2D) {

    if (!(boxCollider2D->IsTrigger || (MyBoxCollider != NULL && MyBoxCollider->IsTrigger)))
        this->velocity->Set(lastPosition->x - gameObject->transform->position->x, lastPosition->y - gameObject->transform->position->y);
}

void Rigidbody::LateUpdate() {
    gameObject->transform->position->Set(gameObject->transform->position->x + this->velocity->x, gameObject->transform->position->y + this->velocity->y);
}


BoxCollider2D::BoxCollider2D(GameObject* gameObject, bool IsTrigger, Vector2* center, Vector2* size, const char* UUID) : MonoBehaviour("BoxCollider2D", gameObject, UUID) {
    this->IsTrigger = IsTrigger;
    this->center = center;
    this->size = size;
    //LstColliders.DeleteAct = false;
    gameObject->scene->LstColliders.Add(this);
};

void BoxCollider2D::Update() {
    if (gameObject->isStatic && !IsTrigger)
        return;
    for (int i = 0; i < gameObject->scene->LstColliders.Count; i++) {
        if (this != gameObject->scene->LstColliders[i] && gameObject->scene->LstColliders[i]->gameObject->IsActive()) {
            int x1 = gameObject->scene->LstColliders[i]->gameObject->transform->position->x +
                gameObject->scene->LstColliders[i]->center->x - (gameObject->scene->LstColliders[i]->size->x / 2);
            int x2 = gameObject->scene->LstColliders[i]->gameObject->transform->position->x +
                gameObject->scene->LstColliders[i]->center->x + (gameObject->scene->LstColliders[i]->size->x / 2);
            int y1 = gameObject->scene->LstColliders[i]->gameObject->transform->position->y +
                gameObject->scene->LstColliders[i]->center->y - (gameObject->scene->LstColliders[i]->size->y / 2);
            int y2 = gameObject->scene->LstColliders[i]->gameObject->transform->position->y +
                gameObject->scene->LstColliders[i]->center->y + (gameObject->scene->LstColliders[i]->size->y / 2);

            int MyX1 = gameObject->transform->position->x + center->x - (size->x / 2);
            int MyX2 = gameObject->transform->position->x + center->x + (size->x / 2);
            int MyY1 = gameObject->transform->position->y + center->y - (size->y / 2);
            int MyY2 = gameObject->transform->position->y + center->y + (size->y / 2);

            if (x1 < MyX2 &&
                x2 > MyX1 &&
                y1 < MyY2 &&
                y2 > MyY1) {
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
void AllFightGolem::Update(){
if (((this->PVplayer)<=(0))){
GameOver();

}
if (((this->PVGolem)<=(0))){
Victory();

}
if (((this->Yplayer)<(0))){
this->Yplayer=0;

}
if (((this->Yplayer)>(50))){
this->Yplayer=50;

}
if (IsKeyDown(KEY_CTRL_UP)){
this->Yplayer+=-5;

}
if (IsKeyDown(KEY_CTRL_DOWN)){
this->Yplayer+=5;

}
PlayerGm->transform->position->y = this->Yplayer;
if (IsKeyDown(KEY_CTRL_EXE)){
EpeeGm->activeSelf=true;

}else {
EpeeGm->activeSelf=false;

}

}
void AllFightGolem::Start(){
this->TypeAttaque=-1;
PlayerGm = gameObject->Find("Player");
EpeeGm = gameObject->Find("Epee");

}
void AllFightGolem::OnRenderObject() {
StrPVplayer = new unsigned char[20];
sprintf((char*)StrPVplayer, "%d", this->PVplayer);
StrPVGolem = new unsigned char[20];
sprintf((char*)StrPVGolem, "%d", this->PVGolem);
PrintMini(20, 0, (unsigned char*)StrPVplayer, MINI_OVER);
PrintMini(100, 55, (unsigned char*)StrPVGolem, MINI_OVER);
PrintMini(0, 55, "EXE pour utiliser l'Epee", MINI_OVER);

}
void AllFightGolem::GameOver() {
ML_rectangle(0, 0, 127, 63, 0, ML_BLACK, ML_BLACK);
PrintMini(40, 30, "Game Over", 2);
PrintMini(25, 55, "Exe pour continuer", 2);
ML_display_vram();
while (IsKeyDown(KEY_CTRL_EXE)){

}
while (!(IsKeyDown(KEY_CTRL_EXE))){

}
LoadScene(this->gameObject->scene,2);
return;

}
void AllFightGolem::Victory() {
PrintMini(40, 30, "Victoire !", 0);
PrintMini(25, 55, "Exe pour continuer", 0);
ML_display_vram();
while (IsKeyDown(KEY_CTRL_EXE)){

}
while (!(IsKeyDown(KEY_CTRL_EXE))){

}
gameObject->scene->sceneManager->_quit = true;

}

void BallGolem::Update(){
if (((this->gameObject->transform->position->x)<(-10))){
this->gameObject->transform->position->x = this->Xrestart;
this->gameObject->transform->position->y =Random(4, 59);
this->Direction=-1;

}else {
this->gameObject->transform->position->x += ((this->vitesse)*(this->Direction));

}

}
void BallGolem::OnRenderObject() {
ML_filled_circle(this->gameObject->transform->position->x, this->gameObject->transform->position->y, 4,ML_BLACK);

}
void BallGolem::OnTriggerEnter2D(BoxCollider2D* boxCollider2D) {
if ((((Component*)boxCollider2D)->gameObject==PlayerGm)){
GameMg->PVplayer--;
this->gameObject->transform->position->x = -300;

}
if ((((Component*)boxCollider2D)->gameObject==EpeeGm)){
this->Direction=2;
this->vitesse+=1;

}
if ((((Component*)boxCollider2D)->gameObject==GolemGm)){
GameMg->PVGolem--;
this->gameObject->transform->position->x = -300;

}

}
void BallGolem::Start(){
PlayerGm=gameObject->Find("Player");
EpeeGm=gameObject->Find("Epee");
GolemGm=gameObject->Find("Golem");
GameMg=((AllFightGolem *)gameObject->Find("GameManager")->GetComponent("AllFightGolem"));

}

void ChangeSceneTrigger::Start(){
MainPlayer = gameObject->Find("Player");

}
void ChangeSceneTrigger::OnTriggerEnter2D(BoxCollider2D* boxCollider2D) {
if ((((Component*)boxCollider2D)->gameObject==MainPlayer)){
LoadScene(this->gameObject->scene,this->SceneNb);
return;

}

}

void Curseur::Update(){
if (IsKeyDown(KEY_CTRL_UP)){
this->gameObject->transform->position->y += -5;

}
if (IsKeyDown(KEY_CTRL_DOWN)){
this->gameObject->transform->position->y += 5;

}
if (IsKeyDown(KEY_CTRL_LEFT)){
this->gameObject->transform->position->x += -5;

}
if (IsKeyDown(KEY_CTRL_RIGHT)){
this->gameObject->transform->position->x += 5;

}
if (((this->gameObject->transform->position->x)>(127))){
this->gameObject->transform->position->x = 127;

}
if (((this->gameObject->transform->position->x)<(0))){
this->gameObject->transform->position->x = 0;

}
if (((this->gameObject->transform->position->y)>(63))){
this->gameObject->transform->position->y = 63;

}
if (((this->gameObject->transform->position->y)<(0))){
this->gameObject->transform->position->y = 0;

}

}

void Dialogue1::Start(){
this->MySprite=((Sprite *)this->gameObject->GetComponent("Sprite"));
StartDialogue();

}
void Dialogue1::WaitExe() {
while (IsKeyDown(KEY_CTRL_EXE)){

}
while (!(IsKeyDown(KEY_CTRL_EXE))){

}

}
void Dialogue1::StartDialogue() {
const char** dialogues;
int* spImg;
if (((this->loadD)==(0))){
const char* dialoguesT[] ={
"Jessy",
"","",
"L'Admin !",
"","",

"Admin",
"Le seul et l'unique!",
"Je me suis tellement",
"amuse pendant notre",
"dernier combat que",
"je n'ai pas pu",

"Admin",
"m'empecher de revenir.",
"","",
"","",

"Petra",
"","",
"Attends c'est vraiment",
"toi l'Admin ?",
"",

"Admin",
"Cet enorme colosse de",
"Prisme marine, ce n'etait",
"qu'une bricole.",
"Je l'ai sorti pour" ,
"l'occasion, amusant non ?",

"Admin",
"J'ai pense que ce serait",
"plus simple de discuter",
"comme ca, oui hein !",
"c'est une grosse peluche.",
"",

"Jessy",
"Minute, c'est comme ca",
"que vous vous amusez ?",
"","",
"",

"Admin",
"Heuu Ouais !",
"Je veux dire toute cette",
"action fracassante et",
"votre tentative desesperee",
"pour secourir les gens,",

"Admin",
"c'etait incroyable, tous",
"les quatre vous avez",
"penetre dans mon temple",
"et vous en etes sortis",
"vivants !",

"Admin",
"Des Heros !",
"vous etes parfaits",
"pour ma creation !",
"","",

"Jessy",
"Ou vous voulez en venir ?",
"","",
"","",

"Admin",
"J'ai un nouveau defi",
"pour vous, crois moi",
"tu vas l'adorer !",
"","",

"Petra",
"Pas encore !",
"","",
"","",

"Admin",
"Tu entends ca ?",
"C'est une vague de",
"destruction fatale",
"categorie diamant qui",
"fonce droit vers la ville.",

"Admin",
"C'est pas mal hien !",
"je l'ai beaucoup",
"peaufinee !",
"","",

"Jessy",
"Je sais que vous avez",
"des plans ou je ne sais",
"quoi mais laissez mes",
"habitants tranquilles",
"ils sont innocents !",

"Admin",
"On dirait que tu tiens",
"beaucoup a eux,",
"ta ville restera enfermee",
"dans la nuit eternelle,",
"tourmentee par des",

"Admin",
"vagues mortelles de",
"monstres jusqu'a ce que",
"tu reprennes cette montre.",
"","",

"Jack",
"Qui se trouve ou ?",
"","",
"","",

"Admin",
"Merci de me le demander",
"","",
"","",

"Admin",
"Elle se trouve tout en",
"haut de mon merveilleux,",
"fantastique et super",
"dangereux palais de glace.",
"",

"Admin",
"C'est simple, il suffit",
"de suivre le chemin,",
"vous ne pouvez pas",
"le manquer.",
"",

"Jessy",
"Vous mettez des",
"innocents en danger",
"pour jouer a vos petits",
"jeux.",
"",

"Admin",
"Et bien techniquement",
"c'est toi qui les mets",
"en danger si tu ne pars",
"pas recuperer la montre.",
"",

"Jessy",
"Qu'est ce que vous",
"attendez de nous ?",
"Pourquoi vous faites",
"tout ca ?",
"",

"Admin",
"Parce que je trouve ca",
"drole bien sur, je sens",
"que ca va etre epique !",
"Je suis sur que vous",
"comprenez...",

"Admin",
"N'oubliez pas, vous",
"trouvez la montre",
"vous sauvez la ville,",
"ciao ciao.",
""}
;
int spImgT[] = {2,1,1,3,1,1,2,1,1,1,2,1,3,1,1,2,1,1,0,1,1,1,2,1,2,1,1};
this->longueur=162;
dialogues=dialoguesT;
spImg=spImgT;

}
if (((this->loadD)==(1))){
const char* dialoguesT[] ={ "Admin", "Bonjour !", "Bonjour tout le monde !", "HA HA !", "Approchez ! Approchez !", "Ne soyez pas timides !", "Jessy", "C'est reparti pour un tour", "","", "","", "Admin", "Hoo ! mais vous etes", "venus en nombre...", "charmant...", "charmant...", "", "Admin", "tes frequentations...", "je ne sais pas trop,", "cet endroit est pour le", "haut du panier,", "", "Admin", "pas pour les...", "comment dire...", "loosers.", "","", "Admin", "Cette structure devant", "vous, sert a designer", "les personnes dignes", "de cette grandeur.", "", "Admin", "A trier les forts et", "les faibles...", "","", "", "Admin", "Alors, voyons ce que", "valent tes petits", "camarades ok ?", "","", "Jessy", "Je ne m'en ferais pas", "trop a ta place parce", "que mes amis sont loin", "d'etre faibles.", "", "Admin", "Super ! Si tu le dis...", "","","","", "Admin", "Allons Jessy ne le", "prends pas mal,", "tout ca c'est pour toi !", "","", "Admin", "Fais attention ou", "tu marches,", "cet endroit fourmille", "de nouvelles creatures.", "", "Admin", "C'est limpide,", "vous voulez tous", "atteindre la montre", "mais seule la creme de", "la creme aura le droit", "Admin", "de faire equipe avec moi a", "l'avenir,", "ca pourrait peut-etre toi.", "","", "Admin", "Bon et si on passait aux", "choses serieuses...", "","","", "", "", "*L'admin ouvre une trappe", "qui fait tomber nos", "personnages*", "", "Tous", "Haaaaaaaaaaaaaaaaa!" "","","","","", };
int spImgT[] ={1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,0,0};
this->longueur=102;
dialogues=dialoguesT;
spImg=spImgT;

}
for (int o =0;o<longueur;o+=6){
ML_clear_vram();
ChangeSprite(spImg[(int)(o/6)]);
MySprite->OnRenderObject();
PrintMini(0, 0, (unsigned char*)dialogues[o], MINI_OVER);
PrintMini(0, 20, (unsigned char*)dialogues[o+1], MINI_OVER);
PrintMini(0, 28, (unsigned char*)dialogues[o+2], MINI_OVER);
PrintMini(0, 36, (unsigned char*)dialogues[o+3], MINI_OVER);
PrintMini(0, 44, (unsigned char*)dialogues[o+4], MINI_OVER);
PrintMini(0, 52, (unsigned char*)dialogues[o+5], MINI_OVER);
ML_display_vram();
WaitExe();

}

}
void Dialogue1::ChangeSprite(int nb) {
if ((nb==0)){
MySprite->image = TextureV;

}
if ((nb==1)){
MySprite->image =Snowman ;

}
if ((nb==2)){
MySprite->image = Jessy;

}
if ((nb==3)){
MySprite->image =Petra ;

}

}
void Dialogue1::Update(){
LoadScene(this->gameObject->scene,this->NextScene);
return;

}

void GameManagerCible::Update(){
if (((this->points)<(0))){
this->points=0;

}
StrPoints = new unsigned char[20];
sprintf((char*)StrPoints, "%d", this->points);
PrintMini(0, 0, (unsigned char*)StrPoints, MINI_OVER);
if (((this->points)>(24))){
LoadScene(this->gameObject->scene,2);
return;

}

}
void GameManagerCible::Start(){
this->points=0;

}

void MainMenu::Update(){
if (((this->frame)<(15))){
this->frame+=1;
return;

}
if (IsKeyDown(KEY_CTRL_EXE)){
this->gameObject->transform->position->x = 200;
this->gameObject->transform->position->y = 200;

}
if (((this->gameObject->transform->position->y)<(100))){
this->gameObject->transform->position->y += 1;

}else {
if (((this->frame)<(30))){
this->frame+=1;
return;

}
continueTxt->activeSelf=true;

}

}
void MainMenu::Start(){
this->gameObject->transform->position->x = 0;
this->gameObject->transform->position->y = 0;
this->frame=0;
continueTxt = gameObject->Find("Continue");

}
void MainMenu::OnRenderObject() {
if (((((this->gameObject->transform->position->x)==(200)))&&(((this->gameObject->transform->position->y)==(200))))){
ML_rectangle(0, 0, 127, 63, 0, ML_BLACK, ML_BLACK);
PrintMini(15, 20, "Le jeu s'adapte aux choix", 2);
PrintMini(30, 28, "que vous faites.", 2);
PrintMini(15, 36, "L'histoire est determinee", 2);
PrintMini(15, 44, "par votre facon de jouer", 2);
if (((this->frame)<(75))){
this->frame+=1;
return;

}else {
LoadScene(this->gameObject->scene,4);
return;

}

}

}

void PlayerController::Update(){
if (IsKeyDown(KEY_CTRL_UP)){
this->gameObject->transform->position->y += ((0)-(this->Vitesse));
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
MySprite->image = Haut1;

}else {
if (((this->Frame)==(1))){
MySprite->image = Haut2;

}else {
MySprite->image = Haut3;

}

}

}else {
if (IsKeyDown(KEY_CTRL_DOWN)){
this->gameObject->transform->position->y += this->Vitesse;
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
MySprite->image = Bas1;

}else {
if (((this->Frame)==(1))){
MySprite->image = Bas2;

}else {
MySprite->image = Bas3;

}

}

}else {
if (IsKeyDown(KEY_CTRL_RIGHT)){
this->gameObject->transform->position->x += this->Vitesse;
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
MySprite->image = Droite1;

}else {
if (((this->Frame)==(1))){
MySprite->image = Droite2;

}else {
MySprite->image = Droite3;

}

}

}else {
if (IsKeyDown(KEY_CTRL_LEFT)){
this->gameObject->transform->position->x += ((0)-(this->Vitesse));
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
MySprite->image = Gauche1;

}else {
if (((this->Frame)==(1))){
MySprite->image = Gauche2;

}else {
MySprite->image = Gauche3;

}

}

}else {
this->Frame=0;

}

}

}

}
this->Frame=mod((int)((this->Frame)+(1)),(int)4);

}
void PlayerController::Start(){
this->Frame=0;
this->MySprite=((Sprite *)this->gameObject->GetComponent("Sprite"));

}
void PlayerController::LateUpdate() {
gameObject->scene->AllCameras[0]->gameObject->transform->position->Set(gameObject->transform->position->x - ((127 / 2) - (MySprite->image->width / 2)), gameObject->transform->position->y - ((63 / 2) - (MySprite->image->height / 2)));

}
void PlayerController::OnRenderObject() {
ML_rectangle((127 / 2) - (12 / 2), (63 / 2) - (20 / 2), (127 / 2) + (12 / 2), (63 / 2) - (20 / 2) +20, 0, ML_WHITE, ML_WHITE);

}

void RoomCible::OnCollisionStay2D(BoxCollider2D* boxCollider2D) {
if (IsKeyDown(KEY_CTRL_EXE)){
if ((IsMonster)){
GameMg->points+=1;

}else {
GameMg->points-=1;

}
this->WaitTime=0;
WaitTime-=Random(0,2);

}

}
void RoomCible::Start(){
GameMg=((GameManagerCible *)gameObject->Find("GameManager")->GetComponent("GameManagerCible"));
this->MySprite=((Sprite *)this->gameObject->GetComponent("Sprite"));
if (((((this->WaitTime)>(0)))&&(((this->WaitTime)<(21))))){
this->gameObject->transform->position->x += 130;

}
if (((this->WaitTime)<(0))){
this->gameObject->transform->position->x += -130;

}
this->NextSprite=mod((int)this->WaitTime,(int)2);

}
void RoomCible::Update(){
if (((this->WaitTime)>(60))){
this->WaitTime=0;
WaitTime-=Random(0,2);
if ((IsMonster)){
GameMg->points-=1;

}

}
if (((this->WaitTime)==(0))){
this->gameObject->transform->position->x += 130;

}
if (((this->WaitTime)==(20))){
Show();

}
this->WaitTime+=1;

}
void RoomCible::Show() {
if (((this->NextSprite)==(0))){
this->NextSprite=1;

}else {
this->NextSprite=0;

}
this->gameObject->transform->position->x += -130;
if ((Random(0,2)==0)){
if (((this->NextSprite)==(0))){
MySprite->image = GameMg->M1;

}else {
MySprite->image = GameMg->M2;

}
IsMonster = true;

}else {
if (((this->NextSprite)==(0))){
MySprite->image = GameMg->V1;

}else {
MySprite->image = GameMg->V2;

}
IsMonster = false;

}

}

