#pragma once
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
#ifndef ClassParticuleEngine
#define ClassParticuleEngine
#include "Announcement.h"
#include "MonochromeLib.h"
#include "List.h"
#include <iostream>
#include <math.h>
#include "usefull.h"
#include "Ressources.h"

int Random(int start, int end);

int LenChar(char* txt);

int mod(int x, int m);

enum Tag;

enum Layer;

class Vector2 {
    //https://docs.unity3d.com/ScriptReference/Vector2.html
public:
    float x;
    float y;
    Vector2();
    Vector2(float x, float y);
    void Set(float x, float y);
    void Set(Vector2 vect);

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

class Component : public Object {
    //https://docs.unity3d.com/ScriptReference/Component.html
public:
    //char* tag;
    GameObject* gameObject;
    //Transform* transform;

    Component(const char* name, GameObject* gameObject, const char* UUID = NULL);

    virtual ~Component() {};

    /*void BroadcastMessage();
    void CompareTag();
    void GetComponent();
    void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void TryGetComponent();*/

    ///
    virtual void PhysicsCalculator() {};
    ///

    virtual void Awake() {}
    virtual void FixedUpdate() {}
    virtual void LateUpdate() {}
    /*virtual void OnAnimatorIK() {}
    virtual void OnAnimatorMove() {}
    virtual void OnApplicationFocus() {}
    virtual void OnApplicationPause() {}
    virtual void OnApplicationQuit() {}
    virtual void OnAudioFilterRead() {}
    virtual void OnBecameInvisible() {}
    virtual void OnBecameVisible() {}*/
    //virtual void OnCollisionEnter() {}
    virtual void OnCollisionEnter2D(BoxCollider2D* boxCollider2D) {}/////
    //virtual void OnCollisionExit() {}
    virtual void OnCollisionExit2D(BoxCollider2D* boxCollider2D) {}//////
    //virtual void OnCollisionStay() {}
    virtual void OnCollisionStay2D(BoxCollider2D* boxCollider2D) {}//////
    //virtual void OnConnectedToServer() {}
    virtual void OnControllerColliderHit() {}//////
    virtual void OnDestroy() {}//////
    virtual void OnDisable() {}//////
    /*virtual void OnDisconnectedFromServer() {}
    virtual void OnDrawGizmos() {}
    virtual void OnDrawGizmosSelected() {}*/
    virtual void OnEnable() {}//////
    //virtual void OnFailedToConnect() {}
    //virtual void OnFailedToConnectToMasterServer() {}
    virtual void OnGUI() {}///////
    /*virtual void OnJointBreak() {}
    virtual void OnJointBreak2D() {}
    virtual void OnMasterServerEvent() {}
    virtual void OnMouseDown() {}
    virtual void OnMouseDrag() {}
    virtual void OnMouseEnter() {}
    virtual void OnMouseExit() {}
    virtual void OnMouseOver() {}
    virtual void OnMouseUp() {}
    virtual void OnMouseUpAsButton() {}
    virtual void OnNetworkInstantiate() {}
    virtual void OnParticleCollision() {}
    virtual void OnParticleSystemStopped() {}
    virtual void OnParticleTrigger() {}
    virtual void OnParticleUpdateJobScheduled() {}
    virtual void OnPlayerConnected() {}
    virtual void OnPlayerDisconnected() {}
    virtual void OnPostRender() {}
    virtual void OnPreCull() {}
    virtual void OnPreRender() {}
    virtual void OnRenderImage() {}*/
    virtual void OnRenderObject() {}
    /*virtual void OnSerializeNetworkView() {}
    virtual void OnServerInitialized() {}
    virtual void OnTransformChildrenChanged() {}
    virtual void OnTransformParentChanged() {}*/
    //virtual void OnTriggerEnter() {}
    virtual void OnTriggerEnter2D(BoxCollider2D* boxCollider2D) {}
    //virtual void OnTriggerExit() {}
    virtual void OnTriggerExit2D(BoxCollider2D* boxCollider2D) {}
    //virtual void OnTriggerStay() {}
    virtual void OnTriggerStay2D(BoxCollider2D* boxCollider2D) {}
    virtual void OnValidate() {}//////
    //virtual void OnWillRenderObject() {}
    virtual void Reset() {}/////
    virtual void Start() {}
    virtual void Update() {}
};
class Transform : public Component {
    //https://docs.unity3d.com/ScriptReference/Transform.html
private:
    Vector2* lastPosition;
public:
    List<Transform*> children;
    int childCount;
    //Vector2* eulerAngles;
    //Vector2* forward;
    bool hasChanged;
    int hierarchyCapacity;
    int hierarchyCount;
    //Vector2* localEulerAngles;
    Vector2* localPosition;
    //Quaternion* localRotation;
    //Vector2* localScale;
    //Matrix4x4* localToWorldMatrix;
    Vector2* lossyScale;
    Transform* parent;
    Vector2* position;
    //Vector2* right;
    //Transform* root;
    //Quaternion* rotation;
    //Vector2* up;
    //Matrix4x4* worldToLocalMatrix;

    Transform(GameObject* gameObject, const char* UUID = NULL, const char* name = "Transform");

    ~Transform() {
        delete lastPosition;
        delete localPosition;
        //delete localScale;
        delete position;
    };

    void SetParent(Transform* transform);

    void Start();

    void Update();
};


class Behaviour : public Component {
    //https://docs.unity3d.com/ScriptReference/Behaviour.html
public:

    bool enabled;
    bool isActiveAndEnabled;
    Behaviour(const char* name, GameObject* gameObject, const char* UUID = NULL);

    virtual ~Behaviour() {};
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


enum TextureDimension;

enum FilterMode;

class Texture : public Object {
    //https://docs.unity3d.com/ScriptReference/Texture.html
public:
    Texture();
    Texture(const char* name, int width, int height, const unsigned char* Data, const char* UUID = NULL);
    unsigned char* textureData;
    /*
    bool allowThreadedTextureCreation;
    int currentTextureMemory;
    int desiredTextureMemory;
    int GenerateAllMips;
    int nonStreamingTextureCount;
    int nonStreamingTextureMemory;
    int streamingMipmapUploadCount;
    int streamingRendererCount;
    int streamingTextureCount;
    bool streamingTextureDiscardUnusedMips;
    bool streamingTextureForceLoadAll;
    int streamingTextureLoadingCount;
    int streamingTexturePendingLoadCount;
    int targetTextureMemory;
    int totalTextureMemory;*/

    //int anisoLevel;
    TextureDimension dimension;
    FilterMode filterMode;
    //graphicsFormat;//https://docs.unity3d.com/ScriptReference/Experimental.Rendering.GraphicsFormat.html
    int height;
    //imageContentsHash;//https://docs.unity3d.com/ScriptReference/Hash128.html
    bool isReadable;
    //float mipMapBias;
    //int mipmapCount;
    //int updateCount;
    int width;
    //wrapMode;//https://docs.unity3d.com/ScriptReference/TextureWrapMode.html
    //wrapModeU;
    //wrapModeV;
    //wrapModeW;

    


};

class MonoBehaviour : public Behaviour {
    //https://docs.unity3d.com/ScriptReference/MonoBehaviour.html
public:
    //runInEditMode c'est pour l'éditeur donc il n'est pas présent
    bool useGUILayout;

    MonoBehaviour(const char* name, GameObject* gameObject, const char* UUID = NULL);

    virtual ~MonoBehaviour() {};

    /*void CancelInvoke();
    void Invoke();
    void InvokeRepeating();
    void IsInvoking();
    void StartCoroutine();
    void StopAllCoroutines();
    void StopCoroutine();*/
    //print c'est pour l'éditeur donc il n'est pas présent
};


class GameObject : public Object {
    //https://docs.unity3d.com/ScriptReference/GameObject.html
public:
    List<Component*> ListOfComponent;
    bool activeInHierarchy;
    bool activeSelf;
    bool isStatic;
    Layer layer;
    Scene* scene;
    long sceneCullingMask;
    Tag tag;
    Transform* transform;

    GameObject(Scene* scene, const char* name, const char* UUID = NULL);

    ~GameObject() {
        for (int i = 0; i < ListOfComponent.Count; i++) {
            delete ListOfComponent.Pop();
        }
        ListOfComponent.Clear();
    };

    bool IsActive();

    void AddComponent(Component* component);
    //void BroadcastMessage();
    //void CompareTag();
    Component* GetComponent(const char* name);
    /*void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void SetActive();
    void TryGetComponent();*/

    //static void CreatePrimitive();
    GameObject* Find(unsigned char* name);
    //static void FindGameObjectsWithTag();
    //static void FindWithTag();
};


class Scene {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.Scene.html
public:
    List<GameObject*> AllGameObject;
    SceneManager* sceneManager;
    List<Camera*> AllCameras;
    List<BoxCollider2D*> LstColliders;
    //void GetRootGameObjects();
    //bool IsValid();

    ~Scene() {
        for (int i = 0; i < AllGameObject.Count; i++) {
            delete AllGameObject.Pop();
        }
        AllGameObject.Clear();
    }

    void AddGameObject(GameObject* gObj);

    void Update();

    void Start();

    int buildIndex;
    //bool isDirty;
    //bool isLoaded;
    char* name;
    //char* path;
    //int rootCount;

    
};

class Camera : public Behaviour {
    //https://docs.unity3d.com/ScriptReference/Camera.html
public:
    Camera(GameObject* gameObject, const char* UUID = NULL);
};

class Image : MonoBehaviour { //: public VisualElement {
    //https://docs.unity3d.com/ScriptReference/UIElements.Image.html
public:
    //unsigned char* ussClassName;
    Texture* image;
    //scaleMode
    //sourceRect
    //tintColor
    //uv
    //vectorImage

    Image(GameObject* gameObject, Texture* image, const char* UUID = NULL);

    void OnRenderObject();
};

class Sprite : MonoBehaviour { //: public VisualElement {
    //https://docs.unity3d.com/ScriptReference/UIElements.Image.html
public:

    Texture* image;


    Sprite(GameObject* gameObject, Texture* image, const char* UUID = NULL);

    void OnRenderObject();
};


class Rigidbody : MonoBehaviour {
private:
    Vector2* lastPosition;
    BoxCollider2D* MyBoxCollider;
public:
    float Mass;
    bool UseGravity;
    bool IsKinematic;
    Vector2* velocity;

    Rigidbody(GameObject* gameObject, float Mass, bool UseGravity, bool IsKinematic, const char* UUID = NULL);

    void PhysicsCalculator();
    void OnCollisionEnter2D(BoxCollider2D* boxCollider2D);
    void OnCollisionStay2D(BoxCollider2D* boxCollider2D);
    void LateUpdate();

    ~Rigidbody() {
        delete velocity;
        delete lastPosition;
    };

    void Start();
    
};


/*class Collider2D : MonoBehaviour {
    //https://docs.unity3d.com/ScriptReference/Collider2D.html
public:
    
};*/

class BoxCollider2D : MonoBehaviour {//Collider2D {
    //https://docs.unity3d.com/ScriptReference/BoxCollider2D.html

private:
    List<BoxCollider2D*> LstColliders;
public:
    bool IsTrigger;
    Vector2* center;
    Vector2* size;

    BoxCollider2D(GameObject* gameObject,bool IsTrigger,Vector2* center,Vector2* size, const char* UUID = NULL);

    void Update() ;

    bool Contains(BoxCollider2D* boxCollider) {
        for (int o = 0; o < LstColliders.Count; o++) {
            if (boxCollider == LstColliders[o])
                return true;
                
        }
        return false;
    };

    ~BoxCollider2D() {
        delete center;
        delete size;
    };
};

class Text : MonoBehaviour {

public:
    unsigned char* text;

    Text(GameObject* gameObject, unsigned char* text, const char* UUID = NULL);

    void OnRenderObject();


};

class Tilemap : MonoBehaviour { 
public:

    Texture** images;
    int* Datas;
    Vector2* sizeTilemap;
    Vector2* sizeCase;


    Tilemap(GameObject* gameObject, Vector2* sizeTilemap, Vector2* sizeCase, const char* UUID = NULL);

    ~Tilemap() {
        delete[] images;
        delete[] Datas;
    };

    void OnRenderObject();
};


class AllFightGolem : MonoBehaviour {
private:
    int TypeAttaque;
int Yplayer;
GameObject* PlayerGm;
GameObject* EpeeGm;
unsigned char* StrPVplayer;
unsigned char* StrPVGolem;

public:
    int PVplayer;
int PVGolem;

    AllFightGolem(GameObject* gameObject ,int PVplayer,int PVGolem, const char* UUID = NULL) : MonoBehaviour("AllFightGolem", gameObject, UUID) {
        this->PVplayer=PVplayer;
this->PVGolem=PVGolem;
this->TypeAttaque=0;
this->Yplayer=0;
this->StrPVplayer="";
this->StrPVGolem="";

    };
    
    void Update(){
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
void Start(){
this->TypeAttaque=-1;
PlayerGm = gameObject->Find("Player");
EpeeGm = gameObject->Find("Epee");

}
void OnRenderObject(){
StrPVplayer = new unsigned char[20];
sprintf((char*)StrPVplayer, "%d", this->PVplayer);
StrPVGolem = new unsigned char[20];
sprintf((char*)StrPVGolem, "%d", this->PVGolem);
PrintMini(20, 0, (unsigned char*)StrPVplayer, MINI_OVER);
PrintMini(100, 55, (unsigned char*)StrPVGolem, MINI_OVER);
PrintMini(0, 55, "EXE pour utiliser l'Epee", MINI_OVER);

}
void GameOver(){
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
void Victory();

};
class BallGolem : MonoBehaviour {
private:
    GameObject* PlayerGm;
GameObject* EpeeGm;
GameObject* GolemGm;
int Direction;
AllFightGolem* GameMg;

public:
    int vitesse;
int Xrestart;

    BallGolem(GameObject* gameObject ,int vitesse,int Xrestart, const char* UUID = NULL) : MonoBehaviour("BallGolem", gameObject, UUID) {
        this->vitesse=vitesse;
this->Xrestart=Xrestart;
this->Direction=0;

    };
    
    void Update(){
if (((this->gameObject->transform->position->x)<(-10))){
this->gameObject->transform->position->x = this->Xrestart;
this->gameObject->transform->position->y =Random(4, 59);
this->Direction=-1;

}else {
this->gameObject->transform->position->x += ((this->vitesse)*(this->Direction));

}

}
void OnRenderObject(){
ML_filled_circle(this->gameObject->transform->position->x, this->gameObject->transform->position->y, 4,ML_BLACK);

}
void OnTriggerEnter2D(BoxCollider2D* boxCollider2D){
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
void Start(){
PlayerGm=gameObject->Find("Player");
EpeeGm=gameObject->Find("Epee");
GolemGm=gameObject->Find("Golem");
GameMg=((AllFightGolem *)gameObject->Find("GameManager")->GetComponent("AllFightGolem"));

}

};
class ChangeSceneTrigger : MonoBehaviour {
private:
    GameObject* MainPlayer;

public:
    int SceneNb;

    ChangeSceneTrigger(GameObject* gameObject ,int SceneNb, const char* UUID = NULL) : MonoBehaviour("ChangeSceneTrigger", gameObject, UUID) {
        this->SceneNb=SceneNb;

    };
    
    void Start(){
MainPlayer = gameObject->Find("Player");

}
void OnTriggerEnter2D(BoxCollider2D* boxCollider2D){
if ((((Component*)boxCollider2D)->gameObject==MainPlayer)){
LoadScene(this->gameObject->scene,this->SceneNb);
return;

}

}

};
class Curseur : MonoBehaviour {
private:
    
public:
    
    Curseur(GameObject* gameObject , const char* UUID = NULL) : MonoBehaviour("Curseur", gameObject, UUID) {
        
    };
    
    void Update(){
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

};
class Dialogue1 : MonoBehaviour {
private:
    Sprite* MySprite;
int longueur;

public:
    int loadD;
int NextScene;
Texture* TextureV;
Texture* Snowman;
Texture* Jessy;
Texture* Petra;

    Dialogue1(GameObject* gameObject ,int loadD,int NextScene,Texture* TextureV,Texture* Snowman,Texture* Jessy,Texture* Petra, const char* UUID = NULL) : MonoBehaviour("Dialogue1", gameObject, UUID) {
        this->loadD=loadD;
this->NextScene=NextScene;
this->TextureV=TextureV;
this->Snowman=Snowman;
this->Jessy=Jessy;
this->Petra=Petra;
this->longueur=0;

    };
    
    void Start(){
this->MySprite=((Sprite *)this->gameObject->GetComponent("Sprite"));
StartDialogue();

}
void WaitExe(){
while (IsKeyDown(KEY_CTRL_EXE)){

}
while (!(IsKeyDown(KEY_CTRL_EXE))){

}

}
void StartDialogue(){
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
void ChangeSprite(int nb){
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
void Update(){
LoadScene(this->gameObject->scene,this->NextScene);
return;

}

};
class GameManagerCible : MonoBehaviour {
private:
    unsigned char* StrPoints;

public:
    int points;
Texture* M1;
Texture* M2;
Texture* V1;
Texture* V2;

    GameManagerCible(GameObject* gameObject ,int points,Texture* M1,Texture* M2,Texture* V1,Texture* V2, const char* UUID = NULL) : MonoBehaviour("GameManagerCible", gameObject, UUID) {
        this->points=points;
this->M1=M1;
this->M2=M2;
this->V1=V1;
this->V2=V2;
this->StrPoints="";

    };
    
    void Update(){
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
void Start(){
this->points=0;

}

};
class MainMenu : MonoBehaviour {
private:
    int frame;
GameObject* continueTxt;

public:
    
    MainMenu(GameObject* gameObject , const char* UUID = NULL) : MonoBehaviour("MainMenu", gameObject, UUID) {
        this->frame=0;

    };
    
    void Update(){
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
void Start(){
this->gameObject->transform->position->x = 0;
this->gameObject->transform->position->y = 0;
this->frame=0;
continueTxt = gameObject->Find("Continue");

}
void OnRenderObject(){
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

};
class PlayerController : MonoBehaviour {
private:
    int Frame;
Sprite* MySprite;

public:
    Texture* Bas1;
Texture* Bas2;
Texture* Bas3;
Texture* Haut1;
Texture* Haut2;
Texture* Haut3;
Texture* Droite1;
Texture* Droite2;
Texture* Droite3;
Texture* Gauche1;
Texture* Gauche2;
Texture* Gauche3;
int Vitesse;

    PlayerController(GameObject* gameObject ,Texture* Bas1,Texture* Bas2,Texture* Bas3,Texture* Haut1,Texture* Haut2,Texture* Haut3,Texture* Droite1,Texture* Droite2,Texture* Droite3,Texture* Gauche1,Texture* Gauche2,Texture* Gauche3,int Vitesse, const char* UUID = NULL) : MonoBehaviour("PlayerController", gameObject, UUID) {
        this->Bas1=Bas1;
this->Bas2=Bas2;
this->Bas3=Bas3;
this->Haut1=Haut1;
this->Haut2=Haut2;
this->Haut3=Haut3;
this->Droite1=Droite1;
this->Droite2=Droite2;
this->Droite3=Droite3;
this->Gauche1=Gauche1;
this->Gauche2=Gauche2;
this->Gauche3=Gauche3;
this->Vitesse=Vitesse;
this->Frame=0;

    };
    
    void Update(){
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
void Start(){
this->Frame=0;
this->MySprite=((Sprite *)this->gameObject->GetComponent("Sprite"));

}
void LateUpdate(){
gameObject->scene->AllCameras[0]->gameObject->transform->position->Set(gameObject->transform->position->x - ((127 / 2) - (MySprite->image->width / 2)), gameObject->transform->position->y - ((63 / 2) - (MySprite->image->height / 2)));

}
void OnRenderObject(){
ML_rectangle((127 / 2) - (12 / 2), (63 / 2) - (20 / 2), (127 / 2) + (12 / 2), (63 / 2) - (20 / 2) +20, 0, ML_WHITE, ML_WHITE);

}

};
class RoomCible : MonoBehaviour {
private:
    GameManagerCible* GameMg;
bool IsMonster;
Sprite* MySprite;
int NextSprite;

public:
    int WaitTime;

    RoomCible(GameObject* gameObject ,int WaitTime, const char* UUID = NULL) : MonoBehaviour("RoomCible", gameObject, UUID) {
        this->WaitTime=WaitTime;
this->IsMonster=false;
this->NextSprite=0;

    };
    
    void OnCollisionStay2D(BoxCollider2D* boxCollider2D){
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
void Start(){
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
void Update(){
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
void Show(){
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

};


class SceneManager {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.html
public:
    int sceneCount;
    static int sceneCountInBuildSettings;
    int LoadSceneAfter;
    bool _quit;
    
    SceneManager() {
        LoadSceneAfter = -1;
        _quit = false;
        LoadTextures();
    }

    //Static Methods
    /*static void CreateScene();
    static void GetActiveScene();
    static void GetSceneAt();
    static void GetSceneByBuildIndex();
    static void GetSceneByName();
    static void GetSceneByPath();*/
    void LoadScene(int index);
    void LoadScene(unsigned char* name);
    /*static void LoadSceneAsync();
    static void MergeScenes();
    static void MoveGameObjectToScene();
    static void SetActiveScene();
    static void UnloadSceneAsync();*/

    GameObject* FindWithName(unsigned char* name);

    //Events
    /*static void activeSceneChanged();
    static void sceneLoaded();
    static void sceneUnloaded();*/

    void UpdateScene();

    void StartScene();

    Texture* Texture_UUID_04fb0cc8_0298_4fab_bd95_5b8d1db85b17;
Texture* Texture_UUID_116d1081_a2c0_43d1_b7bb_81643bad3f94;
Texture* Texture_UUID_147e8f31_a962_42f2_8f91_944a89516c5d;
Texture* Texture_UUID_1859a511_f4d6_4999_9994_45e8d497d0df;
Texture* Texture_UUID_1d46ef84_3ef2_4f07_9bb6_71ce133c4f77;
Texture* Texture_UUID_2816f7e2_9f79_4090_ac47_76c08e39325e;
Texture* Texture_UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c;
Texture* Texture_UUID_3b28f421_9575_4c12_91c4_2c145b435538;
Texture* Texture_UUID_52f16e30_b1a8_408e_9664_d6d710303482;
Texture* Texture_UUID_53848287_45f6_410e_b7f2_b01019c5a1e9;
Texture* Texture_UUID_5a4c0419_e520_4bb8_a707_7b59df2255ed;
Texture* Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af;
Texture* Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea;
Texture* Texture_UUID_66dca2ab_0a08_43fc_a448_2179f34ad86c;
Texture* Texture_UUID_6cc02476_4d75_4e06_b505_3db525f0673d;
Texture* Texture_UUID_76f99faa_8951_464d_9d90_1ea7c1613a87;
Texture* Texture_UUID_7f0a9d09_8937_478e_beda_c09a5dc6790c;
Texture* Texture_UUID_7f68a5a5_ef04_4b1e_8f81_2fd619911c02;
Texture* Texture_UUID_8168c15e_9504_4f14_8a4b_8dbd3406ed5a;
Texture* Texture_UUID_91d54c2d_192d_40d2_ac8f_92d2927aa132;
Texture* Texture_UUID_940f3b9d_a1fe_4c88_842e_6d318b779fee;
Texture* Texture_UUID_99fdda9e_5f7e_47df_a856_d46d34dafdc8;
Texture* Texture_UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae;
Texture* Texture_UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b;
Texture* Texture_UUID_a2f91cb9_ab69_4a03_8aec_ff6494992895;
Texture* Texture_UUID_a790e6b3_c1ad_471e_92e4_89bf7144f584;
Texture* Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6;
Texture* Texture_UUID_b52215f6_7c53_47f5_846d_cee105076be8;
Texture* Texture_UUID_baa0cc40_191d_4b08_87ac_920a06dae3d1;
Texture* Texture_UUID_bfd7e0a7_6527_4f80_90f4_4f0f19ee228c;
Texture* Texture_UUID_bff3df74_a4e3_4eb5_8a30_abff758cf5e1;
Texture* Texture_UUID_ca7908c5_01ca_4c1f_ad49_27462e2fe969;
Texture* Texture_UUID_db658a5f_21f8_4a9b_9532_80c1baab8550;
Texture* Texture_UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f;
Texture* Texture_UUID_e3fe3204_9c0c_4f64_9ccc_601f5a7d8e56;
Texture* Texture_UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f;
Texture* Texture_UUID_e54063c2_f921_4ff1_a44b_7bc8b892cca3;
Texture* Texture_UUID_e870f483_8f84_44ae_b86c_bb1978372306;
Texture* Texture_UUID_edab8e79_8622_4f93_9bb9_333dbd4c1055;
Texture* Texture_UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6;
Texture* Texture_UUID_f0f724e4_cbed_4643_b262_b5a31dde2970;
Texture* Texture_UUID_f5e72803_1505_43a9_9037_9b8670792cdc;
Texture* Texture_UUID_f9063d80_029e_4d13_acab_2a1a33411d34;
Texture* Texture_UUID_fc44d7a1_e5b7_4f80_883f_985c86fa7507;
Texture* Texture_UUID_fcb28c94_39e2_4fa0_94cb_d86a2a8f9ccf;
Texture* Texture_UUID_fd6c944d_3613_486e_a2a8_b1240bc78c4a;
Texture* Texture_UUID_fe0b8a80_7f4c_4f6a_ba1f_407a83ec431e;


private:
    List<Scene*> AllSceneLoaded;

    void LoadTextures() {
        Texture_UUID_04fb0cc8_0298_4fab_bd95_5b8d1db85b17= new Texture("Texture",16,16,UUID_04fb0cc8_0298_4fab_bd95_5b8d1db85b17);
Texture_UUID_116d1081_a2c0_43d1_b7bb_81643bad3f94= new Texture("Texture",50,74,UUID_116d1081_a2c0_43d1_b7bb_81643bad3f94);
Texture_UUID_147e8f31_a962_42f2_8f91_944a89516c5d= new Texture("Texture",15,14,UUID_147e8f31_a962_42f2_8f91_944a89516c5d);
Texture_UUID_1859a511_f4d6_4999_9994_45e8d497d0df= new Texture("Texture",16,16,UUID_1859a511_f4d6_4999_9994_45e8d497d0df);
Texture_UUID_1d46ef84_3ef2_4f07_9bb6_71ce133c4f77= new Texture("Texture",25,20,UUID_1d46ef84_3ef2_4f07_9bb6_71ce133c4f77);
Texture_UUID_2816f7e2_9f79_4090_ac47_76c08e39325e= new Texture("Texture",15,20,UUID_2816f7e2_9f79_4090_ac47_76c08e39325e);
Texture_UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c= new Texture("Texture",16,20,UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c);
Texture_UUID_3b28f421_9575_4c12_91c4_2c145b435538= new Texture("Texture",16,20,UUID_3b28f421_9575_4c12_91c4_2c145b435538);
Texture_UUID_52f16e30_b1a8_408e_9664_d6d710303482= new Texture("Texture",32,58,UUID_52f16e30_b1a8_408e_9664_d6d710303482);
Texture_UUID_53848287_45f6_410e_b7f2_b01019c5a1e9= new Texture("Texture",16,20,UUID_53848287_45f6_410e_b7f2_b01019c5a1e9);
Texture_UUID_5a4c0419_e520_4bb8_a707_7b59df2255ed= new Texture("Texture",16,16,UUID_5a4c0419_e520_4bb8_a707_7b59df2255ed);
Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af= new Texture("Texture",16,20,UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af);
Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea= new Texture("Texture",16,20,UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea);
Texture_UUID_66dca2ab_0a08_43fc_a448_2179f34ad86c= new Texture("Texture",33,63,UUID_66dca2ab_0a08_43fc_a448_2179f34ad86c);
Texture_UUID_6cc02476_4d75_4e06_b505_3db525f0673d= new Texture("Texture",25,60,UUID_6cc02476_4d75_4e06_b505_3db525f0673d);
Texture_UUID_76f99faa_8951_464d_9d90_1ea7c1613a87= new Texture("Texture",16,16,UUID_76f99faa_8951_464d_9d90_1ea7c1613a87);
Texture_UUID_7f0a9d09_8937_478e_beda_c09a5dc6790c= new Texture("Texture",109,100,UUID_7f0a9d09_8937_478e_beda_c09a5dc6790c);
Texture_UUID_7f68a5a5_ef04_4b1e_8f81_2fd619911c02= new Texture("Texture",16,16,UUID_7f68a5a5_ef04_4b1e_8f81_2fd619911c02);
Texture_UUID_8168c15e_9504_4f14_8a4b_8dbd3406ed5a= new Texture("Texture",28,32,UUID_8168c15e_9504_4f14_8a4b_8dbd3406ed5a);
Texture_UUID_91d54c2d_192d_40d2_ac8f_92d2927aa132= new Texture("Texture",18,21,UUID_91d54c2d_192d_40d2_ac8f_92d2927aa132);
Texture_UUID_940f3b9d_a1fe_4c88_842e_6d318b779fee= new Texture("Texture",17,15,UUID_940f3b9d_a1fe_4c88_842e_6d318b779fee);
Texture_UUID_99fdda9e_5f7e_47df_a856_d46d34dafdc8= new Texture("Texture",16,20,UUID_99fdda9e_5f7e_47df_a856_d46d34dafdc8);
Texture_UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae= new Texture("Texture",16,20,UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae);
Texture_UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b= new Texture("Texture",16,20,UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b);
Texture_UUID_a2f91cb9_ab69_4a03_8aec_ff6494992895= new Texture("Texture",127,53,UUID_a2f91cb9_ab69_4a03_8aec_ff6494992895);
Texture_UUID_a790e6b3_c1ad_471e_92e4_89bf7144f584= new Texture("Texture",16,16,UUID_a790e6b3_c1ad_471e_92e4_89bf7144f584);
Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6= new Texture("Texture",16,20,UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6);
Texture_UUID_b52215f6_7c53_47f5_846d_cee105076be8= new Texture("Texture",16,16,UUID_b52215f6_7c53_47f5_846d_cee105076be8);
Texture_UUID_baa0cc40_191d_4b08_87ac_920a06dae3d1= new Texture("Texture",16,16,UUID_baa0cc40_191d_4b08_87ac_920a06dae3d1);
Texture_UUID_bfd7e0a7_6527_4f80_90f4_4f0f19ee228c= new Texture("Texture",16,16,UUID_bfd7e0a7_6527_4f80_90f4_4f0f19ee228c);
Texture_UUID_bff3df74_a4e3_4eb5_8a30_abff758cf5e1= new Texture("Texture",28,59,UUID_bff3df74_a4e3_4eb5_8a30_abff758cf5e1);
Texture_UUID_ca7908c5_01ca_4c1f_ad49_27462e2fe969= new Texture("Texture",16,16,UUID_ca7908c5_01ca_4c1f_ad49_27462e2fe969);
Texture_UUID_db658a5f_21f8_4a9b_9532_80c1baab8550= new Texture("Texture",16,16,UUID_db658a5f_21f8_4a9b_9532_80c1baab8550);
Texture_UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f= new Texture("Texture",16,20,UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f);
Texture_UUID_e3fe3204_9c0c_4f64_9ccc_601f5a7d8e56= new Texture("Texture",145,81,UUID_e3fe3204_9c0c_4f64_9ccc_601f5a7d8e56);
Texture_UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f= new Texture("Texture",16,20,UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f);
Texture_UUID_e54063c2_f921_4ff1_a44b_7bc8b892cca3= new Texture("Texture",16,16,UUID_e54063c2_f921_4ff1_a44b_7bc8b892cca3);
Texture_UUID_e870f483_8f84_44ae_b86c_bb1978372306= new Texture("Texture",16,20,UUID_e870f483_8f84_44ae_b86c_bb1978372306);
Texture_UUID_edab8e79_8622_4f93_9bb9_333dbd4c1055= new Texture("Texture",16,16,UUID_edab8e79_8622_4f93_9bb9_333dbd4c1055);
Texture_UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6= new Texture("Texture",16,20,UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6);
Texture_UUID_f0f724e4_cbed_4643_b262_b5a31dde2970= new Texture("Texture",16,16,UUID_f0f724e4_cbed_4643_b262_b5a31dde2970);
Texture_UUID_f5e72803_1505_43a9_9037_9b8670792cdc= new Texture("Texture",127,37,UUID_f5e72803_1505_43a9_9037_9b8670792cdc);
Texture_UUID_f9063d80_029e_4d13_acab_2a1a33411d34= new Texture("Texture",70,61,UUID_f9063d80_029e_4d13_acab_2a1a33411d34);
Texture_UUID_fc44d7a1_e5b7_4f80_883f_985c86fa7507= new Texture("Texture",16,16,UUID_fc44d7a1_e5b7_4f80_883f_985c86fa7507);
Texture_UUID_fcb28c94_39e2_4fa0_94cb_d86a2a8f9ccf= new Texture("Texture",17,20,UUID_fcb28c94_39e2_4fa0_94cb_d86a2a8f9ccf);
Texture_UUID_fd6c944d_3613_486e_a2a8_b1240bc78c4a= new Texture("Texture",9,9,UUID_fd6c944d_3613_486e_a2a8_b1240bc78c4a);
Texture_UUID_fe0b8a80_7f4c_4f6a_ba1f_407a83ec431e= new Texture("Texture",14,7,UUID_fe0b8a80_7f4c_4f6a_ba1f_407a83ec431e);

    };


    Scene* GetSceneInBuild(int index) {
        Scene* newScene = new Scene();
        newScene->sceneManager = this;

        if (index == 0){
GameObject* UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289;
GameObject* UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0;
GameObject* UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745;
GameObject* UUID_28fae48e_6188_47d4_be51_f10bbafca139;
GameObject* UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172;
GameObject* UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b;
GameObject* UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb;
GameObject* UUID_01f85ec4_2e9f_4081_9de9_b05917743802;
Text* UUID_f3d6b238_7505_46f2_bd72_37ce06598847;

Text* UUID_3fffc8b1_c7fb_448f_a6f8_789efca23c7c;

Text* UUID_8f9e61f5_1434_4240_b737_ae1c58b8e60f;

Text* UUID_ade1f901_8f87_4526_be8a_248365032ee8;

Text* UUID_077f7bd3_819d_423d_869e_3a7e482e06f9;

Sprite* UUID_59dc7ec2_cec9_48b7_8fc3_3db158673509;

Sprite* UUID_c5bcbb4d_c3aa_48d8_afc1_7bbfa0cfcb08;

MainMenu* UUID_e2ec5038_4e04_452d_9c8f_127248adf44f;
Camera* UUID_6faea77e_5361_4abb_aaa2_257f7e372be4;

UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289= new GameObject(newScene, "Camera","UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289");
UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289->activeSelf = true;
UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289->activeInHierarchy = true;
UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289->isStatic = false;
UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289->transform->position->Set(0,0);
UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289);
UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0= new GameObject(newScene, "ParticuleLogo","UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0");
UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0->activeSelf = true;
UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0->activeInHierarchy = true;
UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0->isStatic = false;
UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0->transform->position->Set(0.0,3.0);
UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0->transform->localPosition->Set(0.0,3.0);
newScene->AddGameObject(UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0);
UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745= new GameObject(newScene, "MinecraftLogo","UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745");
UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745->activeSelf = true;
UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745->activeInHierarchy = true;
UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745->isStatic = false;
UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745->transform->position->Set(-1.0,100.0);
UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745->transform->localPosition->Set(-1.0,100.0);
newScene->AddGameObject(UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745);
UUID_28fae48e_6188_47d4_be51_f10bbafca139= new GameObject(newScene, "Text Fait Avec","UUID_28fae48e_6188_47d4_be51_f10bbafca139");
UUID_28fae48e_6188_47d4_be51_f10bbafca139->activeSelf = true;
UUID_28fae48e_6188_47d4_be51_f10bbafca139->activeInHierarchy = true;
UUID_28fae48e_6188_47d4_be51_f10bbafca139->isStatic = false;
UUID_28fae48e_6188_47d4_be51_f10bbafca139->transform->position->Set(55.0,16.0);
UUID_28fae48e_6188_47d4_be51_f10bbafca139->transform->localPosition->Set(55.0,16.0);
newScene->AddGameObject(UUID_28fae48e_6188_47d4_be51_f10bbafca139);
UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172= new GameObject(newScene, "Name","UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172");
UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172->activeSelf = true;
UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172->activeInHierarchy = true;
UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172->isStatic = false;
UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172->transform->position->Set(25,66);
UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172->transform->localPosition->Set(25,66);
newScene->AddGameObject(UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172);
UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b= new GameObject(newScene, "Saison","UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b");
UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b->activeSelf = true;
UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b->activeInHierarchy = true;
UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b->isStatic = false;
UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b->transform->position->Set(44.0,137.0);
UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b->transform->localPosition->Set(44.0,137.0);
newScene->AddGameObject(UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b);
UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb= new GameObject(newScene, "Ice Palace","UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb");
UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb->activeSelf = true;
UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb->activeInHierarchy = true;
UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb->isStatic = false;
UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb->transform->position->Set(44.0,144.0);
UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb->transform->localPosition->Set(44.0,144.0);
newScene->AddGameObject(UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb);
UUID_01f85ec4_2e9f_4081_9de9_b05917743802= new GameObject(newScene, "Continue","UUID_01f85ec4_2e9f_4081_9de9_b05917743802");
UUID_01f85ec4_2e9f_4081_9de9_b05917743802->activeSelf = false;
UUID_01f85ec4_2e9f_4081_9de9_b05917743802->activeInHierarchy = true;
UUID_01f85ec4_2e9f_4081_9de9_b05917743802->isStatic = false;
UUID_01f85ec4_2e9f_4081_9de9_b05917743802->transform->position->Set(32.0,154.0);
UUID_01f85ec4_2e9f_4081_9de9_b05917743802->transform->localPosition->Set(32.0,154.0);
newScene->AddGameObject(UUID_01f85ec4_2e9f_4081_9de9_b05917743802);




UUID_6faea77e_5361_4abb_aaa2_257f7e372be4 = new Camera(UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289,"UUID_6faea77e_5361_4abb_aaa2_257f7e372be4");
UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289->AddComponent((Component*)UUID_6faea77e_5361_4abb_aaa2_257f7e372be4);


UUID_e2ec5038_4e04_452d_9c8f_127248adf44f = new MainMenu(UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289,"UUID_e2ec5038_4e04_452d_9c8f_127248adf44f");
UUID_872fa383_05d0_4ad6_9dd2_bd255eb2f289->AddComponent((Component*)UUID_e2ec5038_4e04_452d_9c8f_127248adf44f);





UUID_c5bcbb4d_c3aa_48d8_afc1_7bbfa0cfcb08 = new Sprite(UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0,Texture_UUID_a2f91cb9_ab69_4a03_8aec_ff6494992895,"UUID_c5bcbb4d_c3aa_48d8_afc1_7bbfa0cfcb08");
UUID_da1bf091_94e7_431c_96f9_2c51ee9c7df0->AddComponent((Component*)UUID_c5bcbb4d_c3aa_48d8_afc1_7bbfa0cfcb08);





UUID_59dc7ec2_cec9_48b7_8fc3_3db158673509 = new Sprite(UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745,Texture_UUID_f5e72803_1505_43a9_9037_9b8670792cdc,"UUID_59dc7ec2_cec9_48b7_8fc3_3db158673509");
UUID_e29a46c6_a420_4477_8c2e_c1c3689cf745->AddComponent((Component*)UUID_59dc7ec2_cec9_48b7_8fc3_3db158673509);





UUID_077f7bd3_819d_423d_869e_3a7e482e06f9 = new Text(UUID_28fae48e_6188_47d4_be51_f10bbafca139,(unsigned char*)"Fait avec:","UUID_077f7bd3_819d_423d_869e_3a7e482e06f9");
UUID_28fae48e_6188_47d4_be51_f10bbafca139->AddComponent((Component*)UUID_077f7bd3_819d_423d_869e_3a7e482e06f9);





UUID_ade1f901_8f87_4526_be8a_248365032ee8 = new Text(UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172,(unsigned char*)"Farhi vous presente","UUID_ade1f901_8f87_4526_be8a_248365032ee8");
UUID_d4cab51b_741c_4ae8_bf84_b5de338d5172->AddComponent((Component*)UUID_ade1f901_8f87_4526_be8a_248365032ee8);





UUID_8f9e61f5_1434_4240_b737_ae1c58b8e60f = new Text(UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b,(unsigned char*)"Season two","UUID_8f9e61f5_1434_4240_b737_ae1c58b8e60f");
UUID_5249b8f5_fc46_4774_9455_388d1ad6ff2b->AddComponent((Component*)UUID_8f9e61f5_1434_4240_b737_ae1c58b8e60f);





UUID_3fffc8b1_c7fb_448f_a6f8_789efca23c7c = new Text(UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb,(unsigned char*)"Ice Palace","UUID_3fffc8b1_c7fb_448f_a6f8_789efca23c7c");
UUID_935eddf3_fd75_4ef3_82b3_2cec3fa6aaeb->AddComponent((Component*)UUID_3fffc8b1_c7fb_448f_a6f8_789efca23c7c);





UUID_f3d6b238_7505_46f2_bd72_37ce06598847 = new Text(UUID_01f85ec4_2e9f_4081_9de9_b05917743802,(unsigned char*)"EXE pour continuer","UUID_f3d6b238_7505_46f2_bd72_37ce06598847");
UUID_01f85ec4_2e9f_4081_9de9_b05917743802->AddComponent((Component*)UUID_f3d6b238_7505_46f2_bd72_37ce06598847);


}if (index == 1){
GameObject* UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca;
GameObject* UUID_400c4826_db9d_4390_963a_d132c010b431;
GameObject* UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46;
GameObject* UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4;
GameObject* UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f;
GameObject* UUID_72471ff6_3c74_47c9_aede_182fb32afd0b;
GameObject* UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a;
GameObject* UUID_38b9880f_7718_42d4_aa9d_39a81cd036df;
GameObject* UUID_d301e0f9_07f5_48e3_9741_19535d842dd1;
GameObject* UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12;
GameObject* UUID_8f9093d0_c681_4129_825e_5cfed9493064;
GameObject* UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7;
GameObject* UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc;
GameObject* UUID_133abf07_ad60_4304_b75b_567181bde7ac;
GameObject* UUID_44140cfe_3755_4c0f_8970_c58bd2149c41;
GameObject* UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79;
GameObject* UUID_ee709694_c436_4666_ae5a_3219b79790d5;
GameObject* UUID_264ab577_b19e_4582_a449_11655b858cb5;
GameObject* UUID_ec8bbca7_9feb_4784_be38_f3723d688805;
GameObject* UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6;
GameObject* UUID_1315f558_2f74_47ff_ba14_c247417ca01b;
GameObject* UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd;
GameObject* UUID_6882a1e2_e669_4373_920a_4cff5601bcab;
GameObject* UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400;
GameObject* UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462;
GameObject* UUID_be061a45_dcdd_4086_b720_b8ba4a887251;
GameObject* UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc;
GameObject* UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2;
GameObject* UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016;
GameObject* UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0;
BoxCollider2D* UUID_cc4fe40e_05f8_4b07_b5b7_3f9e8ee50539;
ChangeSceneTrigger* UUID_e7f93660_ce61_435e_a9e7_e1db28c5b0a1;

Sprite* UUID_7f8f0d11_b23c_4d20_9de8_5dd2dce6ece3;

BoxCollider2D* UUID_cb3665a8_efe6_4080_8aa3_5742b537613c;

BoxCollider2D* UUID_10594a9e_2746_4e19_8c2d_210eb6010bb2;

BoxCollider2D* UUID_e4b2800c_6d92_4a22_8a22_abc63a375ee1;

BoxCollider2D* UUID_ec4e6aed_81a4_467b_bf51_df408a83fe5f;

BoxCollider2D* UUID_d1057474_653c_4b04_bbf8_6a78ddf8d924;

BoxCollider2D* UUID_366030e0_694b_46a9_8c9b_0bdc0b567f18;

BoxCollider2D* UUID_9269e255_3413_4b90_a03c_2d8f143f2d72;

BoxCollider2D* UUID_a675a77f_dd78_410d_bb2b_da876b35d611;

BoxCollider2D* UUID_518da847_a327_4147_9ed9_5ef1d064d085;

BoxCollider2D* UUID_b9861c74_0877_4682_bd0a_74b5f101cdc3;

BoxCollider2D* UUID_d8f9fc79_639d_4127_945c_e28e00d8c3b1;

BoxCollider2D* UUID_4b37e759_ba62_48d9_9981_80d227f4428f;

BoxCollider2D* UUID_b43b7501_20c8_4e5f_aa51_d95e11606aca;

BoxCollider2D* UUID_ad8226dd_2594_4d17_9b77_0dbcb18bc755;

BoxCollider2D* UUID_d0990e38_0465_436e_b0f8_4f4063567528;

BoxCollider2D* UUID_00b32b2b_5ad8_425f_a71b_ec89a9b1060c;

BoxCollider2D* UUID_e908628e_d8d1_41d5_9d11_a71cdff1c0e0;

BoxCollider2D* UUID_f4fd57bb_79b7_4977_9b83_763ed747c68a;

BoxCollider2D* UUID_8d8d6a31_043f_4acf_98b2_50a56a1e4ae4;

BoxCollider2D* UUID_196b0350_a337_4e97_b688_1bf9b28760eb;

BoxCollider2D* UUID_fdb54cb9_b809_414b_a732_55c686e7d431;

BoxCollider2D* UUID_0eccbb43_6d6f_4dd9_bec7_a6c793ae8a5f;

BoxCollider2D* UUID_69a48259_a242_4a82_987a_d88c14fef866;


BoxCollider2D* UUID_87d9aefe_e8d1_4ad3_a3ad_e20e8cec67e0;
Sprite* UUID_132d656c_da13_4f8f_985d_43d6509f26d4;

Camera* UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4;

Rigidbody* UUID_ca9f5c80_03a0_4b51_8333_15cc4b5c52cf;
BoxCollider2D* UUID_f864b348_3f00_42e0_81bf_3fcf3640e625;
Sprite* UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3;
PlayerController* UUID_6640de22_b0db_4537_8522_f3a7a703d68f;

Tilemap* UUID_fbe0964f_80f0_4bb3_9701_3928fd378215;

UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca= new GameObject(newScene, "Tilemap","UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca");
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->activeSelf = true;
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->activeInHierarchy = true;
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->isStatic = true;
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->transform->position->Set(0,0);
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca);
UUID_400c4826_db9d_4390_963a_d132c010b431= new GameObject(newScene, "Player","UUID_400c4826_db9d_4390_963a_d132c010b431");
UUID_400c4826_db9d_4390_963a_d132c010b431->activeSelf = true;
UUID_400c4826_db9d_4390_963a_d132c010b431->activeInHierarchy = true;
UUID_400c4826_db9d_4390_963a_d132c010b431->isStatic = false;
UUID_400c4826_db9d_4390_963a_d132c010b431->transform->position->Set(154.0,272.0);
UUID_400c4826_db9d_4390_963a_d132c010b431->transform->localPosition->Set(154.0,272.0);
newScene->AddGameObject(UUID_400c4826_db9d_4390_963a_d132c010b431);
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46= new GameObject(newScene, "Camera","UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46");
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->activeSelf = true;
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->activeInHierarchy = true;
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->isStatic = false;
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->transform->position->Set(99.0,251.0);
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->transform->localPosition->Set(-55,-21);
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->transform->SetParent(UUID_400c4826_db9d_4390_963a_d132c010b431->transform);newScene->AddGameObject(UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46);
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4= new GameObject(newScene, "Fontaine","UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4");
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4->activeSelf = true;
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4->activeInHierarchy = true;
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4->isStatic = true;
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4->transform->position->Set(134.0,119.0);
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4->transform->localPosition->Set(134.0,119.0);
newScene->AddGameObject(UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4);
UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f= new GameObject(newScene, "collisions","UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f");
UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->activeSelf = true;
UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->activeInHierarchy = true;
UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->isStatic = true;
UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform->position->Set(0.0,0.0);
UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform->localPosition->Set(0.0,0.0);
newScene->AddGameObject(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f);
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b= new GameObject(newScene, "col1","UUID_72471ff6_3c74_47c9_aede_182fb32afd0b");
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b->activeSelf = true;
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b->activeInHierarchy = true;
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b->isStatic = true;
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b->transform->position->Set(24.0,160.0);
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b->transform->localPosition->Set(24.0,160.0);
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_72471ff6_3c74_47c9_aede_182fb32afd0b);
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a= new GameObject(newScene, "col2","UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a");
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a->activeSelf = true;
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a->activeInHierarchy = true;
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a->isStatic = true;
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a->transform->position->Set(40.0,162.0);
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a->transform->localPosition->Set(40.0,162.0);
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a);
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df= new GameObject(newScene, "col3","UUID_38b9880f_7718_42d4_aa9d_39a81cd036df");
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df->activeSelf = true;
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df->activeInHierarchy = true;
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df->isStatic = true;
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df->transform->position->Set(57.0,65.0);
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df->transform->localPosition->Set(57.0,65.0);
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_38b9880f_7718_42d4_aa9d_39a81cd036df);
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1= new GameObject(newScene, "col4","UUID_d301e0f9_07f5_48e3_9741_19535d842dd1");
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1->activeSelf = true;
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1->activeInHierarchy = true;
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1->isStatic = true;
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1->transform->position->Set(89.0,129.0);
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1->transform->localPosition->Set(89.0,129.0);
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_d301e0f9_07f5_48e3_9741_19535d842dd1);
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12= new GameObject(newScene, "col5","UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12");
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12->activeSelf = true;
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12->activeInHierarchy = true;
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12->isStatic = true;
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12->transform->position->Set(105.0,145.0);
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12->transform->localPosition->Set(105.0,145.0);
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12);
UUID_8f9093d0_c681_4129_825e_5cfed9493064= new GameObject(newScene, "col6","UUID_8f9093d0_c681_4129_825e_5cfed9493064");
UUID_8f9093d0_c681_4129_825e_5cfed9493064->activeSelf = true;
UUID_8f9093d0_c681_4129_825e_5cfed9493064->activeInHierarchy = true;
UUID_8f9093d0_c681_4129_825e_5cfed9493064->isStatic = true;
UUID_8f9093d0_c681_4129_825e_5cfed9493064->transform->position->Set(201.0,65.0);
UUID_8f9093d0_c681_4129_825e_5cfed9493064->transform->localPosition->Set(201.0,65.0);
UUID_8f9093d0_c681_4129_825e_5cfed9493064->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_8f9093d0_c681_4129_825e_5cfed9493064);
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7= new GameObject(newScene, "col7","UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7");
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7->activeSelf = true;
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7->activeInHierarchy = true;
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7->isStatic = true;
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7->transform->position->Set(281.0,48.0);
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7->transform->localPosition->Set(281.0,48.0);
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7);
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc= new GameObject(newScene, "col8","UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc");
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc->activeSelf = true;
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc->activeInHierarchy = true;
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc->isStatic = true;
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc->transform->position->Set(297.0,64.0);
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc->transform->localPosition->Set(297.0,64.0);
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc);
UUID_133abf07_ad60_4304_b75b_567181bde7ac= new GameObject(newScene, "col9","UUID_133abf07_ad60_4304_b75b_567181bde7ac");
UUID_133abf07_ad60_4304_b75b_567181bde7ac->activeSelf = true;
UUID_133abf07_ad60_4304_b75b_567181bde7ac->activeInHierarchy = true;
UUID_133abf07_ad60_4304_b75b_567181bde7ac->isStatic = true;
UUID_133abf07_ad60_4304_b75b_567181bde7ac->transform->position->Set(281.0,145.0);
UUID_133abf07_ad60_4304_b75b_567181bde7ac->transform->localPosition->Set(281.0,145.0);
UUID_133abf07_ad60_4304_b75b_567181bde7ac->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_133abf07_ad60_4304_b75b_567181bde7ac);
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41= new GameObject(newScene, "col10","UUID_44140cfe_3755_4c0f_8970_c58bd2149c41");
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41->activeSelf = true;
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41->activeInHierarchy = true;
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41->isStatic = true;
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41->transform->position->Set(217.0,209.0);
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41->transform->localPosition->Set(217.0,209.0);
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_44140cfe_3755_4c0f_8970_c58bd2149c41);
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79= new GameObject(newScene, "col11","UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79");
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79->activeSelf = true;
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79->activeInHierarchy = true;
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79->isStatic = true;
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79->transform->position->Set(233.0,193.0);
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79->transform->localPosition->Set(233.0,193.0);
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79);
UUID_ee709694_c436_4666_ae5a_3219b79790d5= new GameObject(newScene, "col12","UUID_ee709694_c436_4666_ae5a_3219b79790d5");
UUID_ee709694_c436_4666_ae5a_3219b79790d5->activeSelf = true;
UUID_ee709694_c436_4666_ae5a_3219b79790d5->activeInHierarchy = true;
UUID_ee709694_c436_4666_ae5a_3219b79790d5->isStatic = true;
UUID_ee709694_c436_4666_ae5a_3219b79790d5->transform->position->Set(297.0,241.0);
UUID_ee709694_c436_4666_ae5a_3219b79790d5->transform->localPosition->Set(297.0,241.0);
UUID_ee709694_c436_4666_ae5a_3219b79790d5->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_ee709694_c436_4666_ae5a_3219b79790d5);
UUID_264ab577_b19e_4582_a449_11655b858cb5= new GameObject(newScene, "col13","UUID_264ab577_b19e_4582_a449_11655b858cb5");
UUID_264ab577_b19e_4582_a449_11655b858cb5->activeSelf = true;
UUID_264ab577_b19e_4582_a449_11655b858cb5->activeInHierarchy = true;
UUID_264ab577_b19e_4582_a449_11655b858cb5->isStatic = true;
UUID_264ab577_b19e_4582_a449_11655b858cb5->transform->position->Set(24.0,273.0);
UUID_264ab577_b19e_4582_a449_11655b858cb5->transform->localPosition->Set(24.0,273.0);
UUID_264ab577_b19e_4582_a449_11655b858cb5->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_264ab577_b19e_4582_a449_11655b858cb5);
UUID_ec8bbca7_9feb_4784_be38_f3723d688805= new GameObject(newScene, "col14","UUID_ec8bbca7_9feb_4784_be38_f3723d688805");
UUID_ec8bbca7_9feb_4784_be38_f3723d688805->activeSelf = true;
UUID_ec8bbca7_9feb_4784_be38_f3723d688805->activeInHierarchy = true;
UUID_ec8bbca7_9feb_4784_be38_f3723d688805->isStatic = true;
UUID_ec8bbca7_9feb_4784_be38_f3723d688805->transform->position->Set(40.0,288.0);
UUID_ec8bbca7_9feb_4784_be38_f3723d688805->transform->localPosition->Set(40.0,288.0);
UUID_ec8bbca7_9feb_4784_be38_f3723d688805->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_ec8bbca7_9feb_4784_be38_f3723d688805);
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6= new GameObject(newScene, "col15","UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6");
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6->activeSelf = true;
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6->activeInHierarchy = true;
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6->isStatic = true;
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6->transform->position->Set(9.0,169.0);
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6->transform->localPosition->Set(9.0,169.0);
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6);
UUID_1315f558_2f74_47ff_ba14_c247417ca01b= new GameObject(newScene, "col16","UUID_1315f558_2f74_47ff_ba14_c247417ca01b");
UUID_1315f558_2f74_47ff_ba14_c247417ca01b->activeSelf = true;
UUID_1315f558_2f74_47ff_ba14_c247417ca01b->activeInHierarchy = true;
UUID_1315f558_2f74_47ff_ba14_c247417ca01b->isStatic = true;
UUID_1315f558_2f74_47ff_ba14_c247417ca01b->transform->position->Set(313.0,180.0);
UUID_1315f558_2f74_47ff_ba14_c247417ca01b->transform->localPosition->Set(313.0,180.0);
UUID_1315f558_2f74_47ff_ba14_c247417ca01b->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_1315f558_2f74_47ff_ba14_c247417ca01b);
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd= new GameObject(newScene, "col17","UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd");
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd->activeSelf = true;
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd->activeInHierarchy = true;
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd->isStatic = true;
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd->transform->position->Set(27.0,313.0);
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd->transform->localPosition->Set(27.0,313.0);
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd);
UUID_6882a1e2_e669_4373_920a_4cff5601bcab= new GameObject(newScene, "col18","UUID_6882a1e2_e669_4373_920a_4cff5601bcab");
UUID_6882a1e2_e669_4373_920a_4cff5601bcab->activeSelf = true;
UUID_6882a1e2_e669_4373_920a_4cff5601bcab->activeInHierarchy = true;
UUID_6882a1e2_e669_4373_920a_4cff5601bcab->isStatic = true;
UUID_6882a1e2_e669_4373_920a_4cff5601bcab->transform->position->Set(294.0,313.0);
UUID_6882a1e2_e669_4373_920a_4cff5601bcab->transform->localPosition->Set(294.0,313.0);
UUID_6882a1e2_e669_4373_920a_4cff5601bcab->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_6882a1e2_e669_4373_920a_4cff5601bcab);
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400= new GameObject(newScene, "col19","UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400");
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400->activeSelf = true;
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400->activeInHierarchy = true;
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400->isStatic = true;
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400->transform->position->Set(169.0,329.0);
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400->transform->localPosition->Set(169.0,329.0);
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400);
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462= new GameObject(newScene, "col20","UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462");
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462->activeSelf = true;
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462->activeInHierarchy = true;
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462->isStatic = true;
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462->transform->position->Set(46.0,24.0);
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462->transform->localPosition->Set(46.0,24.0);
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462);
UUID_be061a45_dcdd_4086_b720_b8ba4a887251= new GameObject(newScene, "col21","UUID_be061a45_dcdd_4086_b720_b8ba4a887251");
UUID_be061a45_dcdd_4086_b720_b8ba4a887251->activeSelf = true;
UUID_be061a45_dcdd_4086_b720_b8ba4a887251->activeInHierarchy = true;
UUID_be061a45_dcdd_4086_b720_b8ba4a887251->isStatic = true;
UUID_be061a45_dcdd_4086_b720_b8ba4a887251->transform->position->Set(292.0,24.0);
UUID_be061a45_dcdd_4086_b720_b8ba4a887251->transform->localPosition->Set(292.0,24.0);
UUID_be061a45_dcdd_4086_b720_b8ba4a887251->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_be061a45_dcdd_4086_b720_b8ba4a887251);
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc= new GameObject(newScene, "col22","UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc");
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc->activeSelf = true;
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc->activeInHierarchy = true;
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc->isStatic = true;
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc->transform->position->Set(96.0,-16.0);
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc->transform->localPosition->Set(96.0,-16.0);
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc);
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2= new GameObject(newScene, "col23","UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2");
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2->activeSelf = true;
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2->activeInHierarchy = true;
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2->isStatic = true;
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2->transform->position->Set(226.0,-16.0);
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2->transform->localPosition->Set(226.0,-16.0);
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2->transform->SetParent(UUID_35c2dfb9_0da6_4d21_9460_66c3d2b39d6f->transform);newScene->AddGameObject(UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2);
UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016= new GameObject(newScene, "portail","UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016");
UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016->activeSelf = true;
UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016->activeInHierarchy = true;
UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016->isStatic = true;
UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016->transform->position->Set(88.0,-80.0);
UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016->transform->localPosition->Set(88.0,-80.0);
newScene->AddGameObject(UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016);
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0= new GameObject(newScene, "ChangeScene","UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0");
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0->activeSelf = true;
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0->activeInHierarchy = true;
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0->isStatic = false;
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0->transform->position->Set(158.0,-53.0);
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0->transform->localPosition->Set(158.0,-53.0);
newScene->AddGameObject(UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0);




UUID_fbe0964f_80f0_4bb3_9701_3928fd378215 = new Tilemap(UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca,new Vector2(20,20),new Vector2(16,16),"UUID_fbe0964f_80f0_4bb3_9701_3928fd378215");
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->AddComponent((Component*)UUID_fbe0964f_80f0_4bb3_9701_3928fd378215);
static int UUID_fbe0964f_80f0_4bb3_9701_3928fd378215_TilemapDatas[] = {0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 8, 9, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 10, 0, 0, 0, 14, 15, 0, 0, 0, 0, 8, 9, 9, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 14, 14, 0, 0, 0, 0, 0, 0, 1, 8, 0, 7, 11, 0, 1, 0, 0, 0, 0, 15, 15, 15, 0, 1, 0, 0, 0, 0, 2, 1, 6, 7, 0, 0, 2, 0, 0, 0, 0, 14, 14, 15, 0, 2, 0, 0, 0, 0, 13, 2, 6, 7, 0, 0, 0, 0, 0, 15, 14, 15, 15, 14, 0, 0, 0, 0, 14, 0, 0, 0, 6, 7, 0, 0, 0, 0, 0, 14, 15, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 6, 7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6, 7, 2, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 6, 7, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 6, 7, 2, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 13, 14, 11, 0, 1, 2, 0, 0, 0, 0, 6, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 2, 15, 0, 0, 0, 0, 6, 7, 0, 0, 0, 11, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 7, 0, 0, 0, 13, 11, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 7, 2, 1, 14, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 11, 0, 0, 6, 7, 15, 2, 14, 15, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 15, 11, 14, 6, 0, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 0};
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->Datas = UUID_fbe0964f_80f0_4bb3_9701_3928fd378215_TilemapDatas;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images = new Texture * [16];
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[0] = new Texture();
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[1] = Texture_UUID_04fb0cc8_0298_4fab_bd95_5b8d1db85b17;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[2] = Texture_UUID_b52215f6_7c53_47f5_846d_cee105076be8;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[3] = Texture_UUID_e54063c2_f921_4ff1_a44b_7bc8b892cca3;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[4] = Texture_UUID_ca7908c5_01ca_4c1f_ad49_27462e2fe969;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[5] = Texture_UUID_edab8e79_8622_4f93_9bb9_333dbd4c1055;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[6] = Texture_UUID_5a4c0419_e520_4bb8_a707_7b59df2255ed;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[7] = Texture_UUID_fc44d7a1_e5b7_4f80_883f_985c86fa7507;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[8] = Texture_UUID_bfd7e0a7_6527_4f80_90f4_4f0f19ee228c;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[9] = Texture_UUID_f0f724e4_cbed_4643_b262_b5a31dde2970;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[10] = Texture_UUID_a790e6b3_c1ad_471e_92e4_89bf7144f584;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[11] = Texture_UUID_76f99faa_8951_464d_9d90_1ea7c1613a87;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[12] = Texture_UUID_db658a5f_21f8_4a9b_9532_80c1baab8550;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[13] = Texture_UUID_1859a511_f4d6_4999_9994_45e8d497d0df;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[14] = Texture_UUID_7f68a5a5_ef04_4b1e_8f81_2fd619911c02;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[15] = Texture_UUID_baa0cc40_191d_4b08_87ac_920a06dae3d1;





UUID_6640de22_b0db_4537_8522_f3a7a703d68f = new PlayerController(UUID_400c4826_db9d_4390_963a_d132c010b431,Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea,Texture_UUID_53848287_45f6_410e_b7f2_b01019c5a1e9,Texture_UUID_3b28f421_9575_4c12_91c4_2c145b435538,Texture_UUID_e870f483_8f84_44ae_b86c_bb1978372306,Texture_UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c,Texture_UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae,Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af,Texture_UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6,Texture_UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f,Texture_UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f,Texture_UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b,Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6,5,"UUID_6640de22_b0db_4537_8522_f3a7a703d68f");
UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_6640de22_b0db_4537_8522_f3a7a703d68f);


UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3 = new Sprite(UUID_400c4826_db9d_4390_963a_d132c010b431,Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea,"UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3");
UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3);


UUID_f864b348_3f00_42e0_81bf_3fcf3640e625 = new BoxCollider2D(UUID_400c4826_db9d_4390_963a_d132c010b431,false,new Vector2(8,10),new Vector2(8,20),"UUID_f864b348_3f00_42e0_81bf_3fcf3640e625");
UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_f864b348_3f00_42e0_81bf_3fcf3640e625);


UUID_ca9f5c80_03a0_4b51_8333_15cc4b5c52cf = new Rigidbody(UUID_400c4826_db9d_4390_963a_d132c010b431,1,false,false,"UUID_ca9f5c80_03a0_4b51_8333_15cc4b5c52cf");
UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_ca9f5c80_03a0_4b51_8333_15cc4b5c52cf);





UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4 = new Camera(UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46,"UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4");
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->AddComponent((Component*)UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4);





UUID_132d656c_da13_4f8f_985d_43d6509f26d4 = new Sprite(UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4,Texture_UUID_116d1081_a2c0_43d1_b7bb_81643bad3f94,"UUID_132d656c_da13_4f8f_985d_43d6509f26d4");
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4->AddComponent((Component*)UUID_132d656c_da13_4f8f_985d_43d6509f26d4);


UUID_87d9aefe_e8d1_4ad3_a3ad_e20e8cec67e0 = new BoxCollider2D(UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4,false,new Vector2(25,58),new Vector2(50,32),"UUID_87d9aefe_e8d1_4ad3_a3ad_e20e8cec67e0");
UUID_cfc7a355_f2c0_40d3_b0b9_55ea646c7ef4->AddComponent((Component*)UUID_87d9aefe_e8d1_4ad3_a3ad_e20e8cec67e0);








UUID_69a48259_a242_4a82_987a_d88c14fef866 = new BoxCollider2D(UUID_72471ff6_3c74_47c9_aede_182fb32afd0b,false,new Vector2(0,0),new Vector2(16,64),"UUID_69a48259_a242_4a82_987a_d88c14fef866");
UUID_72471ff6_3c74_47c9_aede_182fb32afd0b->AddComponent((Component*)UUID_69a48259_a242_4a82_987a_d88c14fef866);





UUID_0eccbb43_6d6f_4dd9_bec7_a6c793ae8a5f = new BoxCollider2D(UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a,false,new Vector2(0,0),new Vector2(16,32),"UUID_0eccbb43_6d6f_4dd9_bec7_a6c793ae8a5f");
UUID_2e517f41_3b43_4cd4_88f9_25626a952f8a->AddComponent((Component*)UUID_0eccbb43_6d6f_4dd9_bec7_a6c793ae8a5f);





UUID_fdb54cb9_b809_414b_a732_55c686e7d431 = new BoxCollider2D(UUID_38b9880f_7718_42d4_aa9d_39a81cd036df,false,new Vector2(0,0),new Vector2(16,32),"UUID_fdb54cb9_b809_414b_a732_55c686e7d431");
UUID_38b9880f_7718_42d4_aa9d_39a81cd036df->AddComponent((Component*)UUID_fdb54cb9_b809_414b_a732_55c686e7d431);





UUID_196b0350_a337_4e97_b688_1bf9b28760eb = new BoxCollider2D(UUID_d301e0f9_07f5_48e3_9741_19535d842dd1,false,new Vector2(0,0),new Vector2(16,32),"UUID_196b0350_a337_4e97_b688_1bf9b28760eb");
UUID_d301e0f9_07f5_48e3_9741_19535d842dd1->AddComponent((Component*)UUID_196b0350_a337_4e97_b688_1bf9b28760eb);





UUID_8d8d6a31_043f_4acf_98b2_50a56a1e4ae4 = new BoxCollider2D(UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12,false,new Vector2(0,0),new Vector2(16,32),"UUID_8d8d6a31_043f_4acf_98b2_50a56a1e4ae4");
UUID_b2c37f69_b544_4eee_b2b8_5e7897ab9b12->AddComponent((Component*)UUID_8d8d6a31_043f_4acf_98b2_50a56a1e4ae4);





UUID_f4fd57bb_79b7_4977_9b83_763ed747c68a = new BoxCollider2D(UUID_8f9093d0_c681_4129_825e_5cfed9493064,false,new Vector2(0,0),new Vector2(16,32),"UUID_f4fd57bb_79b7_4977_9b83_763ed747c68a");
UUID_8f9093d0_c681_4129_825e_5cfed9493064->AddComponent((Component*)UUID_f4fd57bb_79b7_4977_9b83_763ed747c68a);





UUID_e908628e_d8d1_41d5_9d11_a71cdff1c0e0 = new BoxCollider2D(UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7,false,new Vector2(0,0),new Vector2(16,32),"UUID_e908628e_d8d1_41d5_9d11_a71cdff1c0e0");
UUID_aff8ab73_a3b4_4b8e_ac92_1c7326179ef7->AddComponent((Component*)UUID_e908628e_d8d1_41d5_9d11_a71cdff1c0e0);





UUID_00b32b2b_5ad8_425f_a71b_ec89a9b1060c = new BoxCollider2D(UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc,false,new Vector2(0,0),new Vector2(16,32),"UUID_00b32b2b_5ad8_425f_a71b_ec89a9b1060c");
UUID_810b21fd_d536_42f5_b45a_6fd9b3c9b0bc->AddComponent((Component*)UUID_00b32b2b_5ad8_425f_a71b_ec89a9b1060c);





UUID_d0990e38_0465_436e_b0f8_4f4063567528 = new BoxCollider2D(UUID_133abf07_ad60_4304_b75b_567181bde7ac,false,new Vector2(0,0),new Vector2(16,32),"UUID_d0990e38_0465_436e_b0f8_4f4063567528");
UUID_133abf07_ad60_4304_b75b_567181bde7ac->AddComponent((Component*)UUID_d0990e38_0465_436e_b0f8_4f4063567528);





UUID_ad8226dd_2594_4d17_9b77_0dbcb18bc755 = new BoxCollider2D(UUID_44140cfe_3755_4c0f_8970_c58bd2149c41,false,new Vector2(0,0),new Vector2(16,32),"UUID_ad8226dd_2594_4d17_9b77_0dbcb18bc755");
UUID_44140cfe_3755_4c0f_8970_c58bd2149c41->AddComponent((Component*)UUID_ad8226dd_2594_4d17_9b77_0dbcb18bc755);





UUID_b43b7501_20c8_4e5f_aa51_d95e11606aca = new BoxCollider2D(UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79,false,new Vector2(0,0),new Vector2(16,32),"UUID_b43b7501_20c8_4e5f_aa51_d95e11606aca");
UUID_26e60dbf_c4ed_41ee_acdb_c189ec433b79->AddComponent((Component*)UUID_b43b7501_20c8_4e5f_aa51_d95e11606aca);





UUID_4b37e759_ba62_48d9_9981_80d227f4428f = new BoxCollider2D(UUID_ee709694_c436_4666_ae5a_3219b79790d5,false,new Vector2(0,0),new Vector2(16,32),"UUID_4b37e759_ba62_48d9_9981_80d227f4428f");
UUID_ee709694_c436_4666_ae5a_3219b79790d5->AddComponent((Component*)UUID_4b37e759_ba62_48d9_9981_80d227f4428f);





UUID_d8f9fc79_639d_4127_945c_e28e00d8c3b1 = new BoxCollider2D(UUID_264ab577_b19e_4582_a449_11655b858cb5,false,new Vector2(0,0),new Vector2(16,32),"UUID_d8f9fc79_639d_4127_945c_e28e00d8c3b1");
UUID_264ab577_b19e_4582_a449_11655b858cb5->AddComponent((Component*)UUID_d8f9fc79_639d_4127_945c_e28e00d8c3b1);





UUID_b9861c74_0877_4682_bd0a_74b5f101cdc3 = new BoxCollider2D(UUID_ec8bbca7_9feb_4784_be38_f3723d688805,false,new Vector2(0,0),new Vector2(16,32),"UUID_b9861c74_0877_4682_bd0a_74b5f101cdc3");
UUID_ec8bbca7_9feb_4784_be38_f3723d688805->AddComponent((Component*)UUID_b9861c74_0877_4682_bd0a_74b5f101cdc3);





UUID_518da847_a327_4147_9ed9_5ef1d064d085 = new BoxCollider2D(UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6,false,new Vector2(0,0),new Vector2(16,280),"UUID_518da847_a327_4147_9ed9_5ef1d064d085");
UUID_de1ee104_e04e_4d95_ab86_87642dbf08c6->AddComponent((Component*)UUID_518da847_a327_4147_9ed9_5ef1d064d085);





UUID_a675a77f_dd78_410d_bb2b_da876b35d611 = new BoxCollider2D(UUID_1315f558_2f74_47ff_ba14_c247417ca01b,false,new Vector2(0,0),new Vector2(16,280),"UUID_a675a77f_dd78_410d_bb2b_da876b35d611");
UUID_1315f558_2f74_47ff_ba14_c247417ca01b->AddComponent((Component*)UUID_a675a77f_dd78_410d_bb2b_da876b35d611);





UUID_9269e255_3413_4b90_a03c_2d8f143f2d72 = new BoxCollider2D(UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd,false,new Vector2(0,0),new Vector2(200,16),"UUID_9269e255_3413_4b90_a03c_2d8f143f2d72");
UUID_798786c4_ab56_4b4b_b1e2_6c37320523cd->AddComponent((Component*)UUID_9269e255_3413_4b90_a03c_2d8f143f2d72);





UUID_366030e0_694b_46a9_8c9b_0bdc0b567f18 = new BoxCollider2D(UUID_6882a1e2_e669_4373_920a_4cff5601bcab,false,new Vector2(0,0),new Vector2(200,16),"UUID_366030e0_694b_46a9_8c9b_0bdc0b567f18");
UUID_6882a1e2_e669_4373_920a_4cff5601bcab->AddComponent((Component*)UUID_366030e0_694b_46a9_8c9b_0bdc0b567f18);





UUID_d1057474_653c_4b04_bbf8_6a78ddf8d924 = new BoxCollider2D(UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400,false,new Vector2(0,0),new Vector2(200,16),"UUID_d1057474_653c_4b04_bbf8_6a78ddf8d924");
UUID_35a86cd6_d0f7_4a10_ab28_e0d868e13400->AddComponent((Component*)UUID_d1057474_653c_4b04_bbf8_6a78ddf8d924);





UUID_ec4e6aed_81a4_467b_bf51_df408a83fe5f = new BoxCollider2D(UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462,false,new Vector2(0,0),new Vector2(100,16),"UUID_ec4e6aed_81a4_467b_bf51_df408a83fe5f");
UUID_2cea4c5c_162a_47b5_abf4_be0c98b86462->AddComponent((Component*)UUID_ec4e6aed_81a4_467b_bf51_df408a83fe5f);





UUID_e4b2800c_6d92_4a22_8a22_abc63a375ee1 = new BoxCollider2D(UUID_be061a45_dcdd_4086_b720_b8ba4a887251,false,new Vector2(0,0),new Vector2(100,16),"UUID_e4b2800c_6d92_4a22_8a22_abc63a375ee1");
UUID_be061a45_dcdd_4086_b720_b8ba4a887251->AddComponent((Component*)UUID_e4b2800c_6d92_4a22_8a22_abc63a375ee1);





UUID_10594a9e_2746_4e19_8c2d_210eb6010bb2 = new BoxCollider2D(UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc,false,new Vector2(0,0),new Vector2(32,64),"UUID_10594a9e_2746_4e19_8c2d_210eb6010bb2");
UUID_d48b2bd1_4444_482e_b1e0_2828c233fdbc->AddComponent((Component*)UUID_10594a9e_2746_4e19_8c2d_210eb6010bb2);





UUID_cb3665a8_efe6_4080_8aa3_5742b537613c = new BoxCollider2D(UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2,false,new Vector2(0,0),new Vector2(32,64),"UUID_cb3665a8_efe6_4080_8aa3_5742b537613c");
UUID_ff29f8b8_c43d_481d_88d0_ef6568d461a2->AddComponent((Component*)UUID_cb3665a8_efe6_4080_8aa3_5742b537613c);





UUID_7f8f0d11_b23c_4d20_9de8_5dd2dce6ece3 = new Sprite(UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016,Texture_UUID_e3fe3204_9c0c_4f64_9ccc_601f5a7d8e56,"UUID_7f8f0d11_b23c_4d20_9de8_5dd2dce6ece3");
UUID_6ee4b8f0_6cd0_49dc_87f1_9a00a92c6016->AddComponent((Component*)UUID_7f8f0d11_b23c_4d20_9de8_5dd2dce6ece3);





UUID_e7f93660_ce61_435e_a9e7_e1db28c5b0a1 = new ChangeSceneTrigger(UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0,5,"UUID_e7f93660_ce61_435e_a9e7_e1db28c5b0a1");
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0->AddComponent((Component*)UUID_e7f93660_ce61_435e_a9e7_e1db28c5b0a1);


UUID_cc4fe40e_05f8_4b07_b5b7_3f9e8ee50539 = new BoxCollider2D(UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0,true,new Vector2(0,0),new Vector2(120,32),"UUID_cc4fe40e_05f8_4b07_b5b7_3f9e8ee50539");
UUID_5662e19b_88d9_4c2b_a993_ea3b26f30ff0->AddComponent((Component*)UUID_cc4fe40e_05f8_4b07_b5b7_3f9e8ee50539);


}if (index == 2){
GameObject* UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b;
GameObject* UUID_40d9429b_9220_42df_b285_874fccdd63a6;
GameObject* UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1;
GameObject* UUID_427099bd_199b_476d_b893_82d0671fea9a;
GameObject* UUID_851cd880_a470_4162_9198_68fbfce3a525;
GameObject* UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf;
BoxCollider2D* UUID_92116f57_17fd_42cc_9eee_5a453a199970;
BallGolem* UUID_cf8e88cc_12c9_4dda_b1c4_7d5855f57f39;

AllFightGolem* UUID_a9ee3bb1_8cb2_4b52_90f4_70416aca5b06;

BoxCollider2D* UUID_2a8e3ac8_cfeb_4ac5_9109_117c6d6c0741;
Sprite* UUID_c55c6630_d679_49a4_8725_e9a94f86b7b1;

BoxCollider2D* UUID_1cc627cb_5e5a_44f1_866b_94184411f939;
Sprite* UUID_3f3461f1_60d2_4c6c_9213_c282d3f210e3;

BoxCollider2D* UUID_a4655fa1_983f_47ed_ad3a_4cb73e58af58;
Sprite* UUID_e8cb015e_35d1_4a40_9388_7d34342acd53;

Camera* UUID_504247a3_6927_462b_bdd2_3630d13c1e81;

UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b= new GameObject(newScene, "camera","UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b");
UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b->activeSelf = true;
UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b->activeInHierarchy = true;
UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b->isStatic = false;
UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b->transform->position->Set(0,0);
UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b);
UUID_40d9429b_9220_42df_b285_874fccdd63a6= new GameObject(newScene, "Golem","UUID_40d9429b_9220_42df_b285_874fccdd63a6");
UUID_40d9429b_9220_42df_b285_874fccdd63a6->activeSelf = true;
UUID_40d9429b_9220_42df_b285_874fccdd63a6->activeInHierarchy = true;
UUID_40d9429b_9220_42df_b285_874fccdd63a6->isStatic = false;
UUID_40d9429b_9220_42df_b285_874fccdd63a6->transform->position->Set(55.0,0.0);
UUID_40d9429b_9220_42df_b285_874fccdd63a6->transform->localPosition->Set(55.0,0.0);
newScene->AddGameObject(UUID_40d9429b_9220_42df_b285_874fccdd63a6);
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1= new GameObject(newScene, "Player","UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1");
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->activeSelf = true;
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->activeInHierarchy = true;
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->isStatic = false;
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->transform->position->Set(-2.0,1.0);
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->transform->localPosition->Set(-2.0,1.0);
newScene->AddGameObject(UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1);
UUID_427099bd_199b_476d_b893_82d0671fea9a= new GameObject(newScene, "Epee","UUID_427099bd_199b_476d_b893_82d0671fea9a");
UUID_427099bd_199b_476d_b893_82d0671fea9a->activeSelf = true;
UUID_427099bd_199b_476d_b893_82d0671fea9a->activeInHierarchy = true;
UUID_427099bd_199b_476d_b893_82d0671fea9a->isStatic = false;
UUID_427099bd_199b_476d_b893_82d0671fea9a->transform->position->Set(9.0,8.0);
UUID_427099bd_199b_476d_b893_82d0671fea9a->transform->localPosition->Set(11.0,7.0);
UUID_427099bd_199b_476d_b893_82d0671fea9a->transform->SetParent(UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->transform);newScene->AddGameObject(UUID_427099bd_199b_476d_b893_82d0671fea9a);
UUID_851cd880_a470_4162_9198_68fbfce3a525= new GameObject(newScene, "GameManager","UUID_851cd880_a470_4162_9198_68fbfce3a525");
UUID_851cd880_a470_4162_9198_68fbfce3a525->activeSelf = true;
UUID_851cd880_a470_4162_9198_68fbfce3a525->activeInHierarchy = true;
UUID_851cd880_a470_4162_9198_68fbfce3a525->isStatic = false;
UUID_851cd880_a470_4162_9198_68fbfce3a525->transform->position->Set(0,0);
UUID_851cd880_a470_4162_9198_68fbfce3a525->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_851cd880_a470_4162_9198_68fbfce3a525);
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf= new GameObject(newScene, "Ball1","UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf");
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf->activeSelf = true;
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf->activeInHierarchy = true;
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf->isStatic = false;
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf->transform->position->Set(-23.0,9.0);
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf->transform->localPosition->Set(-23.0,9.0);
newScene->AddGameObject(UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf);




UUID_504247a3_6927_462b_bdd2_3630d13c1e81 = new Camera(UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b,"UUID_504247a3_6927_462b_bdd2_3630d13c1e81");
UUID_3abca82c_b048_4ceb_a0d3_b7e98628211b->AddComponent((Component*)UUID_504247a3_6927_462b_bdd2_3630d13c1e81);





UUID_e8cb015e_35d1_4a40_9388_7d34342acd53 = new Sprite(UUID_40d9429b_9220_42df_b285_874fccdd63a6,Texture_UUID_f9063d80_029e_4d13_acab_2a1a33411d34,"UUID_e8cb015e_35d1_4a40_9388_7d34342acd53");
UUID_40d9429b_9220_42df_b285_874fccdd63a6->AddComponent((Component*)UUID_e8cb015e_35d1_4a40_9388_7d34342acd53);


UUID_a4655fa1_983f_47ed_ad3a_4cb73e58af58 = new BoxCollider2D(UUID_40d9429b_9220_42df_b285_874fccdd63a6,false,new Vector2(40,30),new Vector2(30,80),"UUID_a4655fa1_983f_47ed_ad3a_4cb73e58af58");
UUID_40d9429b_9220_42df_b285_874fccdd63a6->AddComponent((Component*)UUID_a4655fa1_983f_47ed_ad3a_4cb73e58af58);





UUID_3f3461f1_60d2_4c6c_9213_c282d3f210e3 = new Sprite(UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1,Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af,"UUID_3f3461f1_60d2_4c6c_9213_c282d3f210e3");
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->AddComponent((Component*)UUID_3f3461f1_60d2_4c6c_9213_c282d3f210e3);


UUID_1cc627cb_5e5a_44f1_866b_94184411f939 = new BoxCollider2D(UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1,false,new Vector2(7,10),new Vector2(8,20),"UUID_1cc627cb_5e5a_44f1_866b_94184411f939");
UUID_d00131d5_cf74_4b20_82bd_b6a0de9f3eb1->AddComponent((Component*)UUID_1cc627cb_5e5a_44f1_866b_94184411f939);





UUID_c55c6630_d679_49a4_8725_e9a94f86b7b1 = new Sprite(UUID_427099bd_199b_476d_b893_82d0671fea9a,Texture_UUID_fe0b8a80_7f4c_4f6a_ba1f_407a83ec431e,"UUID_c55c6630_d679_49a4_8725_e9a94f86b7b1");
UUID_427099bd_199b_476d_b893_82d0671fea9a->AddComponent((Component*)UUID_c55c6630_d679_49a4_8725_e9a94f86b7b1);


UUID_2a8e3ac8_cfeb_4ac5_9109_117c6d6c0741 = new BoxCollider2D(UUID_427099bd_199b_476d_b893_82d0671fea9a,false,new Vector2(7,3),new Vector2(14,7),"UUID_2a8e3ac8_cfeb_4ac5_9109_117c6d6c0741");
UUID_427099bd_199b_476d_b893_82d0671fea9a->AddComponent((Component*)UUID_2a8e3ac8_cfeb_4ac5_9109_117c6d6c0741);





UUID_a9ee3bb1_8cb2_4b52_90f4_70416aca5b06 = new AllFightGolem(UUID_851cd880_a470_4162_9198_68fbfce3a525,3,10,"UUID_a9ee3bb1_8cb2_4b52_90f4_70416aca5b06");
UUID_851cd880_a470_4162_9198_68fbfce3a525->AddComponent((Component*)UUID_a9ee3bb1_8cb2_4b52_90f4_70416aca5b06);





UUID_cf8e88cc_12c9_4dda_b1c4_7d5855f57f39 = new BallGolem(UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf,3,67,"UUID_cf8e88cc_12c9_4dda_b1c4_7d5855f57f39");
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf->AddComponent((Component*)UUID_cf8e88cc_12c9_4dda_b1c4_7d5855f57f39);


UUID_92116f57_17fd_42cc_9eee_5a453a199970 = new BoxCollider2D(UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf,true,new Vector2(0,0),new Vector2(8,8),"UUID_92116f57_17fd_42cc_9eee_5a453a199970");
UUID_e8e2b44a_dcf9_40ce_b3ba_52250f401abf->AddComponent((Component*)UUID_92116f57_17fd_42cc_9eee_5a453a199970);


}if (index == 3){
GameObject* UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d;
GameObject* UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd;
GameObject* UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492;
GameObject* UUID_5e95388a_97a3_406e_9146_873a9532156c;
GameObject* UUID_657194be_07dd_4fc8_916a_003372261788;
GameObject* UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22;
GameObject* UUID_5146af40_db37_4ba2_9de3_fe9d38383e45;
GameObject* UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe;
GameObject* UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19;
GameObject* UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d;
GameObject* UUID_a274cdc6_9816_4994_bbf6_5d987cf08030;
GameObject* UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832;
GameObject* UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924;
GameObject* UUID_c764e89c_d49c_421f_ac37_13893fea9c68;
GameObject* UUID_8468a707_e08d_4550_91e1_daf63430bf51;
GameObject* UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a;
GameObject* UUID_4d3dee37_3f34_4933_a377_4c223b149cf8;
GameObject* UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f;
GameObject* UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59;
GameObject* UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7;
GameObject* UUID_677a2764_7c64_4476_b493_cb597fd3e804;
GameManagerCible* UUID_a7906565_6726_46ff_800b_8ea928fd239c;

Sprite* UUID_5b970a50_55d2_48fb_9c21_66d9fe15025f;

Sprite* UUID_65a99471_7536_4214_b2f4_14a1b1f75b95;

Sprite* UUID_636e142f_acbb_4b60_a628_62cb709cb630;

Sprite* UUID_5a8c2977_590a_43a5_9a02_68fb4985333d;

Sprite* UUID_69c40174_595a_4002_8b68_39d9dabd1762;

Sprite* UUID_97d24a99_3217_406c_9a06_d9aaf282c711;

Sprite* UUID_373ccf3f_5117_4ca6_b931_7b0441f55ed1;

Sprite* UUID_51826a79_03f5_477e_aaa7_593d754db99a;

Sprite* UUID_819ea20a_0c72_410e_8abc_3f0de0d2902c;

Sprite* UUID_9dda8ddb_c219_459f_8d89_9472af518241;

Sprite* UUID_843368b8_a736_4d15_a899_3bd86bc57cf2;


BoxCollider2D* UUID_bf3db7b6_1a90_4f07_aae8_521c152a5bd1;
RoomCible* UUID_8914dc31_b39b_4e0d_a265_85d64a02acc1;
Sprite* UUID_17eae3f2_96ec_4571_ab83_c045725f6c2a;

BoxCollider2D* UUID_d365de6b_8d69_440d_a04c_d9158bdbcdbc;
RoomCible* UUID_50d2ad62_184a_4fb0_995e_c6b0c7c9582a;
Sprite* UUID_c0612cea_f654_4834_9bdd_3c773cbe3c5d;

BoxCollider2D* UUID_c94951fb_940b_4de9_b21d_5809a5883dfe;
RoomCible* UUID_be9ed48f_e81a_448b_a8aa_c8a676f8d95f;
Sprite* UUID_35f27c2d_8356_4eb8_9c24_420306107a7c;

BoxCollider2D* UUID_1547abfa_6377_4dae_b0cf_e5ba2702f104;
RoomCible* UUID_802c1790_7694_4c00_894f_455ef9ffcf4e;
Sprite* UUID_611bea51_5d8d_43fa_9495_9274f23b5a9a;

BoxCollider2D* UUID_214033f9_0b7b_4891_bb49_2e8b341dcbe3;
RoomCible* UUID_11f1fe67_6ed6_4d13_8b8e_563d715a030b;
Sprite* UUID_758240cb_d152_4062_80e2_71d157208fd3;

BoxCollider2D* UUID_68c6d78c_0b4b_4999_859a_9c86f39b83fa;
RoomCible* UUID_b1a1eaac_0de6_4747_910f_82ee0104ce85;
Sprite* UUID_904bdb55_d1cd_4b02_a0a3_ae2ce3f108dd;

BoxCollider2D* UUID_048936d3_1ef8_40aa_a380_22b395ce4d37;
Sprite* UUID_e295595c_9540_4992_b334_c57b4e342609;
Curseur* UUID_310727cc_db94_47f2_ad70_f6b43c907836;

Camera* UUID_f6c2b34f_b14c_4465_a621_db7903109948;

UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d= new GameObject(newScene, "Camera","UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d");
UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d->activeSelf = true;
UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d->activeInHierarchy = true;
UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d->isStatic = false;
UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d->transform->position->Set(0,0);
UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d);
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd= new GameObject(newScene, "Curseur","UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd");
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->activeSelf = true;
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->activeInHierarchy = true;
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->isStatic = false;
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->transform->position->Set(38.0,27.0);
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->transform->localPosition->Set(38.0,27.0);
newScene->AddGameObject(UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd);
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492= new GameObject(newScene, "Cible1","UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492");
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->activeSelf = true;
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->activeInHierarchy = true;
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->isStatic = false;
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->transform->position->Set(57.0,31.0);
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->transform->localPosition->Set(57.0,31.0);
newScene->AddGameObject(UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492);
UUID_5e95388a_97a3_406e_9146_873a9532156c= new GameObject(newScene, "Cible2","UUID_5e95388a_97a3_406e_9146_873a9532156c");
UUID_5e95388a_97a3_406e_9146_873a9532156c->activeSelf = true;
UUID_5e95388a_97a3_406e_9146_873a9532156c->activeInHierarchy = true;
UUID_5e95388a_97a3_406e_9146_873a9532156c->isStatic = false;
UUID_5e95388a_97a3_406e_9146_873a9532156c->transform->position->Set(109.0,17.0);
UUID_5e95388a_97a3_406e_9146_873a9532156c->transform->localPosition->Set(109.0,17.0);
newScene->AddGameObject(UUID_5e95388a_97a3_406e_9146_873a9532156c);
UUID_657194be_07dd_4fc8_916a_003372261788= new GameObject(newScene, "Cible3","UUID_657194be_07dd_4fc8_916a_003372261788");
UUID_657194be_07dd_4fc8_916a_003372261788->activeSelf = true;
UUID_657194be_07dd_4fc8_916a_003372261788->activeInHierarchy = true;
UUID_657194be_07dd_4fc8_916a_003372261788->isStatic = false;
UUID_657194be_07dd_4fc8_916a_003372261788->transform->position->Set(61.0,2.0);
UUID_657194be_07dd_4fc8_916a_003372261788->transform->localPosition->Set(61.0,2.0);
newScene->AddGameObject(UUID_657194be_07dd_4fc8_916a_003372261788);
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22= new GameObject(newScene, "Cible4","UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22");
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->activeSelf = true;
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->activeInHierarchy = true;
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->isStatic = false;
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->transform->position->Set(22.0,4.0);
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->transform->localPosition->Set(22.0,4.0);
newScene->AddGameObject(UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22);
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45= new GameObject(newScene, "Cible5","UUID_5146af40_db37_4ba2_9de3_fe9d38383e45");
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->activeSelf = true;
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->activeInHierarchy = true;
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->isStatic = false;
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->transform->position->Set(16.0,38.0);
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->transform->localPosition->Set(16.0,38.0);
newScene->AddGameObject(UUID_5146af40_db37_4ba2_9de3_fe9d38383e45);
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe= new GameObject(newScene, "Cible6","UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe");
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->activeSelf = true;
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->activeInHierarchy = true;
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->isStatic = false;
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->transform->position->Set(90.0,4.0);
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->transform->localPosition->Set(90.0,4.0);
newScene->AddGameObject(UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe);
UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19= new GameObject(newScene, "Objs","UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19");
UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->activeSelf = true;
UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->activeInHierarchy = true;
UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->isStatic = false;
UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform->position->Set(0,0);
UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19);
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d= new GameObject(newScene, "Arbre","UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d");
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d->activeSelf = true;
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d->activeInHierarchy = true;
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d->isStatic = false;
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d->transform->position->Set(89.0,21.0);
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d->transform->localPosition->Set(89.0,21.0);
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d);
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030= new GameObject(newScene, "Arbre 2","UUID_a274cdc6_9816_4994_bbf6_5d987cf08030");
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030->activeSelf = true;
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030->activeInHierarchy = true;
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030->isStatic = false;
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030->transform->position->Set(7.0,4.0);
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030->transform->localPosition->Set(7.0,4.0);
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_a274cdc6_9816_4994_bbf6_5d987cf08030);
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832= new GameObject(newScene, "barriere1","UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832");
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832->activeSelf = true;
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832->activeInHierarchy = true;
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832->isStatic = false;
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832->transform->position->Set(47.0,16.0);
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832->transform->localPosition->Set(47.0,16.0);
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832);
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924= new GameObject(newScene, "barriere1 (1)","UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924");
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924->activeSelf = true;
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924->activeInHierarchy = true;
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924->isStatic = false;
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924->transform->position->Set(62.0,16.0);
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924->transform->localPosition->Set(62.0,16.0);
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924);
UUID_c764e89c_d49c_421f_ac37_13893fea9c68= new GameObject(newScene, "Mur","UUID_c764e89c_d49c_421f_ac37_13893fea9c68");
UUID_c764e89c_d49c_421f_ac37_13893fea9c68->activeSelf = true;
UUID_c764e89c_d49c_421f_ac37_13893fea9c68->activeInHierarchy = true;
UUID_c764e89c_d49c_421f_ac37_13893fea9c68->isStatic = false;
UUID_c764e89c_d49c_421f_ac37_13893fea9c68->transform->position->Set(76.0,16.0);
UUID_c764e89c_d49c_421f_ac37_13893fea9c68->transform->localPosition->Set(76.0,16.0);
UUID_c764e89c_d49c_421f_ac37_13893fea9c68->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_c764e89c_d49c_421f_ac37_13893fea9c68);
UUID_8468a707_e08d_4550_91e1_daf63430bf51= new GameObject(newScene, "Mur (1)","UUID_8468a707_e08d_4550_91e1_daf63430bf51");
UUID_8468a707_e08d_4550_91e1_daf63430bf51->activeSelf = true;
UUID_8468a707_e08d_4550_91e1_daf63430bf51->activeInHierarchy = true;
UUID_8468a707_e08d_4550_91e1_daf63430bf51->isStatic = false;
UUID_8468a707_e08d_4550_91e1_daf63430bf51->transform->position->Set(76.0,2.0);
UUID_8468a707_e08d_4550_91e1_daf63430bf51->transform->localPosition->Set(76.0,2.0);
UUID_8468a707_e08d_4550_91e1_daf63430bf51->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_8468a707_e08d_4550_91e1_daf63430bf51);
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a= new GameObject(newScene, "barriere1 (2)","UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a");
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a->activeSelf = true;
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a->activeInHierarchy = true;
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a->isStatic = false;
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a->transform->position->Set(33.0,16.0);
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a->transform->localPosition->Set(33.0,16.0);
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a);
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8= new GameObject(newScene, "rocher","UUID_4d3dee37_3f34_4933_a377_4c223b149cf8");
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8->activeSelf = true;
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8->activeInHierarchy = true;
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8->isStatic = false;
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8->transform->position->Set(11.0,49.0);
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8->transform->localPosition->Set(11.0,49.0);
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_4d3dee37_3f34_4933_a377_4c223b149cf8);
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f= new GameObject(newScene, "rocher (1)","UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f");
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f->activeSelf = true;
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f->activeInHierarchy = true;
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f->isStatic = false;
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f->transform->position->Set(-1.0,48.0);
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f->transform->localPosition->Set(-1.0,48.0);
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f);
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59= new GameObject(newScene, "fleur","UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59");
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59->activeSelf = true;
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59->activeInHierarchy = true;
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59->isStatic = false;
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59->transform->position->Set(69.0,40.0);
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59->transform->localPosition->Set(69.0,40.0);
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59);
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7= new GameObject(newScene, "fleur (1)","UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7");
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7->activeSelf = true;
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7->activeInHierarchy = true;
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7->isStatic = false;
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7->transform->position->Set(46.0,40.0);
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7->transform->localPosition->Set(46.0,40.0);
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7->transform->SetParent(UUID_cdf733f9_c712_44ae_84a2_6b72b2c46d19->transform);newScene->AddGameObject(UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7);
UUID_677a2764_7c64_4476_b493_cb597fd3e804= new GameObject(newScene, "GameManager","UUID_677a2764_7c64_4476_b493_cb597fd3e804");
UUID_677a2764_7c64_4476_b493_cb597fd3e804->activeSelf = true;
UUID_677a2764_7c64_4476_b493_cb597fd3e804->activeInHierarchy = true;
UUID_677a2764_7c64_4476_b493_cb597fd3e804->isStatic = false;
UUID_677a2764_7c64_4476_b493_cb597fd3e804->transform->position->Set(0,0);
UUID_677a2764_7c64_4476_b493_cb597fd3e804->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_677a2764_7c64_4476_b493_cb597fd3e804);




UUID_f6c2b34f_b14c_4465_a621_db7903109948 = new Camera(UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d,"UUID_f6c2b34f_b14c_4465_a621_db7903109948");
UUID_a9b7bfa6_eaf8_4c58_a4fa_2c0c5f11217d->AddComponent((Component*)UUID_f6c2b34f_b14c_4465_a621_db7903109948);





UUID_310727cc_db94_47f2_ad70_f6b43c907836 = new Curseur(UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd,"UUID_310727cc_db94_47f2_ad70_f6b43c907836");
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->AddComponent((Component*)UUID_310727cc_db94_47f2_ad70_f6b43c907836);


UUID_e295595c_9540_4992_b334_c57b4e342609 = new Sprite(UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd,Texture_UUID_fd6c944d_3613_486e_a2a8_b1240bc78c4a,"UUID_e295595c_9540_4992_b334_c57b4e342609");
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->AddComponent((Component*)UUID_e295595c_9540_4992_b334_c57b4e342609);


UUID_048936d3_1ef8_40aa_a380_22b395ce4d37 = new BoxCollider2D(UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd,true,new Vector2(4,4),new Vector2(5,5),"UUID_048936d3_1ef8_40aa_a380_22b395ce4d37");
UUID_38af3510_d773_4e65_9ef4_080b4dcda1fd->AddComponent((Component*)UUID_048936d3_1ef8_40aa_a380_22b395ce4d37);





UUID_904bdb55_d1cd_4b02_a0a3_ae2ce3f108dd = new Sprite(UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492,Texture_UUID_2816f7e2_9f79_4090_ac47_76c08e39325e,"UUID_904bdb55_d1cd_4b02_a0a3_ae2ce3f108dd");
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->AddComponent((Component*)UUID_904bdb55_d1cd_4b02_a0a3_ae2ce3f108dd);


UUID_b1a1eaac_0de6_4747_910f_82ee0104ce85 = new RoomCible(UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492,3,"UUID_b1a1eaac_0de6_4747_910f_82ee0104ce85");
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->AddComponent((Component*)UUID_b1a1eaac_0de6_4747_910f_82ee0104ce85);


UUID_68c6d78c_0b4b_4999_859a_9c86f39b83fa = new BoxCollider2D(UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492,false,new Vector2(7,10),new Vector2(15,20),"UUID_68c6d78c_0b4b_4999_859a_9c86f39b83fa");
UUID_0cd33e37_7ec8_4e68_b477_f6f558d8c492->AddComponent((Component*)UUID_68c6d78c_0b4b_4999_859a_9c86f39b83fa);





UUID_758240cb_d152_4062_80e2_71d157208fd3 = new Sprite(UUID_5e95388a_97a3_406e_9146_873a9532156c,Texture_UUID_2816f7e2_9f79_4090_ac47_76c08e39325e,"UUID_758240cb_d152_4062_80e2_71d157208fd3");
UUID_5e95388a_97a3_406e_9146_873a9532156c->AddComponent((Component*)UUID_758240cb_d152_4062_80e2_71d157208fd3);


UUID_11f1fe67_6ed6_4d13_8b8e_563d715a030b = new RoomCible(UUID_5e95388a_97a3_406e_9146_873a9532156c,0,"UUID_11f1fe67_6ed6_4d13_8b8e_563d715a030b");
UUID_5e95388a_97a3_406e_9146_873a9532156c->AddComponent((Component*)UUID_11f1fe67_6ed6_4d13_8b8e_563d715a030b);


UUID_214033f9_0b7b_4891_bb49_2e8b341dcbe3 = new BoxCollider2D(UUID_5e95388a_97a3_406e_9146_873a9532156c,false,new Vector2(7,10),new Vector2(15,20),"UUID_214033f9_0b7b_4891_bb49_2e8b341dcbe3");
UUID_5e95388a_97a3_406e_9146_873a9532156c->AddComponent((Component*)UUID_214033f9_0b7b_4891_bb49_2e8b341dcbe3);





UUID_611bea51_5d8d_43fa_9495_9274f23b5a9a = new Sprite(UUID_657194be_07dd_4fc8_916a_003372261788,Texture_UUID_fcb28c94_39e2_4fa0_94cb_d86a2a8f9ccf,"UUID_611bea51_5d8d_43fa_9495_9274f23b5a9a");
UUID_657194be_07dd_4fc8_916a_003372261788->AddComponent((Component*)UUID_611bea51_5d8d_43fa_9495_9274f23b5a9a);


UUID_802c1790_7694_4c00_894f_455ef9ffcf4e = new RoomCible(UUID_657194be_07dd_4fc8_916a_003372261788,5,"UUID_802c1790_7694_4c00_894f_455ef9ffcf4e");
UUID_657194be_07dd_4fc8_916a_003372261788->AddComponent((Component*)UUID_802c1790_7694_4c00_894f_455ef9ffcf4e);


UUID_1547abfa_6377_4dae_b0cf_e5ba2702f104 = new BoxCollider2D(UUID_657194be_07dd_4fc8_916a_003372261788,false,new Vector2(8,10),new Vector2(17,20),"UUID_1547abfa_6377_4dae_b0cf_e5ba2702f104");
UUID_657194be_07dd_4fc8_916a_003372261788->AddComponent((Component*)UUID_1547abfa_6377_4dae_b0cf_e5ba2702f104);





UUID_35f27c2d_8356_4eb8_9c24_420306107a7c = new Sprite(UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22,Texture_UUID_1d46ef84_3ef2_4f07_9bb6_71ce133c4f77,"UUID_35f27c2d_8356_4eb8_9c24_420306107a7c");
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->AddComponent((Component*)UUID_35f27c2d_8356_4eb8_9c24_420306107a7c);


UUID_be9ed48f_e81a_448b_a8aa_c8a676f8d95f = new RoomCible(UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22,0,"UUID_be9ed48f_e81a_448b_a8aa_c8a676f8d95f");
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->AddComponent((Component*)UUID_be9ed48f_e81a_448b_a8aa_c8a676f8d95f);


UUID_c94951fb_940b_4de9_b21d_5809a5883dfe = new BoxCollider2D(UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22,false,new Vector2(12,10),new Vector2(25,20),"UUID_c94951fb_940b_4de9_b21d_5809a5883dfe");
UUID_ac0cfd3a_9c37_4770_a4d0_31bab0f7ff22->AddComponent((Component*)UUID_c94951fb_940b_4de9_b21d_5809a5883dfe);





UUID_c0612cea_f654_4834_9bdd_3c773cbe3c5d = new Sprite(UUID_5146af40_db37_4ba2_9de3_fe9d38383e45,Texture_UUID_99fdda9e_5f7e_47df_a856_d46d34dafdc8,"UUID_c0612cea_f654_4834_9bdd_3c773cbe3c5d");
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->AddComponent((Component*)UUID_c0612cea_f654_4834_9bdd_3c773cbe3c5d);


UUID_50d2ad62_184a_4fb0_995e_c6b0c7c9582a = new RoomCible(UUID_5146af40_db37_4ba2_9de3_fe9d38383e45,-5,"UUID_50d2ad62_184a_4fb0_995e_c6b0c7c9582a");
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->AddComponent((Component*)UUID_50d2ad62_184a_4fb0_995e_c6b0c7c9582a);


UUID_d365de6b_8d69_440d_a04c_d9158bdbcdbc = new BoxCollider2D(UUID_5146af40_db37_4ba2_9de3_fe9d38383e45,false,new Vector2(8,10),new Vector2(16,20),"UUID_d365de6b_8d69_440d_a04c_d9158bdbcdbc");
UUID_5146af40_db37_4ba2_9de3_fe9d38383e45->AddComponent((Component*)UUID_d365de6b_8d69_440d_a04c_d9158bdbcdbc);





UUID_17eae3f2_96ec_4571_ab83_c045725f6c2a = new Sprite(UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe,Texture_UUID_99fdda9e_5f7e_47df_a856_d46d34dafdc8,"UUID_17eae3f2_96ec_4571_ab83_c045725f6c2a");
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->AddComponent((Component*)UUID_17eae3f2_96ec_4571_ab83_c045725f6c2a);


UUID_8914dc31_b39b_4e0d_a265_85d64a02acc1 = new RoomCible(UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe,10,"UUID_8914dc31_b39b_4e0d_a265_85d64a02acc1");
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->AddComponent((Component*)UUID_8914dc31_b39b_4e0d_a265_85d64a02acc1);


UUID_bf3db7b6_1a90_4f07_aae8_521c152a5bd1 = new BoxCollider2D(UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe,false,new Vector2(8,10),new Vector2(16,20),"UUID_bf3db7b6_1a90_4f07_aae8_521c152a5bd1");
UUID_2aae61f8_d811_4a4d_874d_d4ddf3148afe->AddComponent((Component*)UUID_bf3db7b6_1a90_4f07_aae8_521c152a5bd1);








UUID_843368b8_a736_4d15_a899_3bd86bc57cf2 = new Sprite(UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d,Texture_UUID_8168c15e_9504_4f14_8a4b_8dbd3406ed5a,"UUID_843368b8_a736_4d15_a899_3bd86bc57cf2");
UUID_09dcdff2_9283_4c24_bfd1_248a2b085e2d->AddComponent((Component*)UUID_843368b8_a736_4d15_a899_3bd86bc57cf2);





UUID_9dda8ddb_c219_459f_8d89_9472af518241 = new Sprite(UUID_a274cdc6_9816_4994_bbf6_5d987cf08030,Texture_UUID_8168c15e_9504_4f14_8a4b_8dbd3406ed5a,"UUID_9dda8ddb_c219_459f_8d89_9472af518241");
UUID_a274cdc6_9816_4994_bbf6_5d987cf08030->AddComponent((Component*)UUID_9dda8ddb_c219_459f_8d89_9472af518241);





UUID_819ea20a_0c72_410e_8abc_3f0de0d2902c = new Sprite(UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832,Texture_UUID_147e8f31_a962_42f2_8f91_944a89516c5d,"UUID_819ea20a_0c72_410e_8abc_3f0de0d2902c");
UUID_76ec1d5c_9e91_4e0c_818a_2b09197f4832->AddComponent((Component*)UUID_819ea20a_0c72_410e_8abc_3f0de0d2902c);





UUID_51826a79_03f5_477e_aaa7_593d754db99a = new Sprite(UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924,Texture_UUID_147e8f31_a962_42f2_8f91_944a89516c5d,"UUID_51826a79_03f5_477e_aaa7_593d754db99a");
UUID_aa358dc1_7b99_4619_88d0_5c9dd23b5924->AddComponent((Component*)UUID_51826a79_03f5_477e_aaa7_593d754db99a);





UUID_373ccf3f_5117_4ca6_b931_7b0441f55ed1 = new Sprite(UUID_c764e89c_d49c_421f_ac37_13893fea9c68,Texture_UUID_940f3b9d_a1fe_4c88_842e_6d318b779fee,"UUID_373ccf3f_5117_4ca6_b931_7b0441f55ed1");
UUID_c764e89c_d49c_421f_ac37_13893fea9c68->AddComponent((Component*)UUID_373ccf3f_5117_4ca6_b931_7b0441f55ed1);





UUID_97d24a99_3217_406c_9a06_d9aaf282c711 = new Sprite(UUID_8468a707_e08d_4550_91e1_daf63430bf51,Texture_UUID_940f3b9d_a1fe_4c88_842e_6d318b779fee,"UUID_97d24a99_3217_406c_9a06_d9aaf282c711");
UUID_8468a707_e08d_4550_91e1_daf63430bf51->AddComponent((Component*)UUID_97d24a99_3217_406c_9a06_d9aaf282c711);





UUID_69c40174_595a_4002_8b68_39d9dabd1762 = new Sprite(UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a,Texture_UUID_147e8f31_a962_42f2_8f91_944a89516c5d,"UUID_69c40174_595a_4002_8b68_39d9dabd1762");
UUID_15d3b7cf_c215_4b68_88f8_2d9a9acb308a->AddComponent((Component*)UUID_69c40174_595a_4002_8b68_39d9dabd1762);





UUID_5a8c2977_590a_43a5_9a02_68fb4985333d = new Sprite(UUID_4d3dee37_3f34_4933_a377_4c223b149cf8,Texture_UUID_76f99faa_8951_464d_9d90_1ea7c1613a87,"UUID_5a8c2977_590a_43a5_9a02_68fb4985333d");
UUID_4d3dee37_3f34_4933_a377_4c223b149cf8->AddComponent((Component*)UUID_5a8c2977_590a_43a5_9a02_68fb4985333d);





UUID_636e142f_acbb_4b60_a628_62cb709cb630 = new Sprite(UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f,Texture_UUID_76f99faa_8951_464d_9d90_1ea7c1613a87,"UUID_636e142f_acbb_4b60_a628_62cb709cb630");
UUID_929b3f25_42c3_442d_a5ea_879cfb065f4f->AddComponent((Component*)UUID_636e142f_acbb_4b60_a628_62cb709cb630);





UUID_65a99471_7536_4214_b2f4_14a1b1f75b95 = new Sprite(UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59,Texture_UUID_1859a511_f4d6_4999_9994_45e8d497d0df,"UUID_65a99471_7536_4214_b2f4_14a1b1f75b95");
UUID_09cb5e36_3dc9_40d6_8037_f435bab83c59->AddComponent((Component*)UUID_65a99471_7536_4214_b2f4_14a1b1f75b95);





UUID_5b970a50_55d2_48fb_9c21_66d9fe15025f = new Sprite(UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7,Texture_UUID_940f3b9d_a1fe_4c88_842e_6d318b779fee,"UUID_5b970a50_55d2_48fb_9c21_66d9fe15025f");
UUID_4c83ebc9_3f67_40c2_80cb_d8677df8d3e7->AddComponent((Component*)UUID_5b970a50_55d2_48fb_9c21_66d9fe15025f);





UUID_a7906565_6726_46ff_800b_8ea928fd239c = new GameManagerCible(UUID_677a2764_7c64_4476_b493_cb597fd3e804,0,Texture_UUID_2816f7e2_9f79_4090_ac47_76c08e39325e,Texture_UUID_fcb28c94_39e2_4fa0_94cb_d86a2a8f9ccf,Texture_UUID_1d46ef84_3ef2_4f07_9bb6_71ce133c4f77,Texture_UUID_99fdda9e_5f7e_47df_a856_d46d34dafdc8,"UUID_a7906565_6726_46ff_800b_8ea928fd239c");
UUID_677a2764_7c64_4476_b493_cb597fd3e804->AddComponent((Component*)UUID_a7906565_6726_46ff_800b_8ea928fd239c);


}if (index == 4){
GameObject* UUID_f80b4179_fbef_458a_b43f_598db402e7ce;
GameObject* UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5;
Sprite* UUID_327a64ae_21d5_4290_819b_4fbd87aa9f15;
Dialogue1* UUID_34059c05_df3e_45ff_8922_858b23748cb3;

Camera* UUID_7908b6b6_b109_4959_a413_ff7389cf7754;

UUID_f80b4179_fbef_458a_b43f_598db402e7ce= new GameObject(newScene, "Camera","UUID_f80b4179_fbef_458a_b43f_598db402e7ce");
UUID_f80b4179_fbef_458a_b43f_598db402e7ce->activeSelf = true;
UUID_f80b4179_fbef_458a_b43f_598db402e7ce->activeInHierarchy = true;
UUID_f80b4179_fbef_458a_b43f_598db402e7ce->isStatic = false;
UUID_f80b4179_fbef_458a_b43f_598db402e7ce->transform->position->Set(0,0);
UUID_f80b4179_fbef_458a_b43f_598db402e7ce->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_f80b4179_fbef_458a_b43f_598db402e7ce);
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5= new GameObject(newScene, "SpriteGm","UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5");
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5->activeSelf = true;
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5->activeInHierarchy = true;
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5->isStatic = false;
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5->transform->position->Set(93.0,3.0);
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5->transform->localPosition->Set(93.0,3.0);
newScene->AddGameObject(UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5);




UUID_7908b6b6_b109_4959_a413_ff7389cf7754 = new Camera(UUID_f80b4179_fbef_458a_b43f_598db402e7ce,"UUID_7908b6b6_b109_4959_a413_ff7389cf7754");
UUID_f80b4179_fbef_458a_b43f_598db402e7ce->AddComponent((Component*)UUID_7908b6b6_b109_4959_a413_ff7389cf7754);





UUID_34059c05_df3e_45ff_8922_858b23748cb3 = new Dialogue1(UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5,0,1,new Texture(),Texture_UUID_bff3df74_a4e3_4eb5_8a30_abff758cf5e1,Texture_UUID_52f16e30_b1a8_408e_9664_d6d710303482,Texture_UUID_6cc02476_4d75_4e06_b505_3db525f0673d,"UUID_34059c05_df3e_45ff_8922_858b23748cb3");
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5->AddComponent((Component*)UUID_34059c05_df3e_45ff_8922_858b23748cb3);


UUID_327a64ae_21d5_4290_819b_4fbd87aa9f15 = new Sprite(UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5,Texture_UUID_bff3df74_a4e3_4eb5_8a30_abff758cf5e1,"UUID_327a64ae_21d5_4290_819b_4fbd87aa9f15");
UUID_6bd7b986_677e_438c_a97a_b4c44365eaa5->AddComponent((Component*)UUID_327a64ae_21d5_4290_819b_4fbd87aa9f15);


}if (index == 5){
GameObject* UUID_4321ac20_5110_4607_a401_ff9ec21160f4;
GameObject* UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b;
Dialogue1* UUID_d90fec20_2a7f_4d6a_9323_585d33720a0a;
Sprite* UUID_6a8b88ad_7d82_444a_acd6_5bda54cd21ce;

Camera* UUID_b1b1fa7c_7304_4c64_a329_f58c0255fab6;

UUID_4321ac20_5110_4607_a401_ff9ec21160f4= new GameObject(newScene, "Camera","UUID_4321ac20_5110_4607_a401_ff9ec21160f4");
UUID_4321ac20_5110_4607_a401_ff9ec21160f4->activeSelf = true;
UUID_4321ac20_5110_4607_a401_ff9ec21160f4->activeInHierarchy = true;
UUID_4321ac20_5110_4607_a401_ff9ec21160f4->isStatic = false;
UUID_4321ac20_5110_4607_a401_ff9ec21160f4->transform->position->Set(0,0);
UUID_4321ac20_5110_4607_a401_ff9ec21160f4->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_4321ac20_5110_4607_a401_ff9ec21160f4);
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b= new GameObject(newScene, "Dialogue","UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b");
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b->activeSelf = true;
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b->activeInHierarchy = true;
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b->isStatic = false;
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b->transform->position->Set(93,3);
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b->transform->localPosition->Set(93,3);
newScene->AddGameObject(UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b);




UUID_b1b1fa7c_7304_4c64_a329_f58c0255fab6 = new Camera(UUID_4321ac20_5110_4607_a401_ff9ec21160f4,"UUID_b1b1fa7c_7304_4c64_a329_f58c0255fab6");
UUID_4321ac20_5110_4607_a401_ff9ec21160f4->AddComponent((Component*)UUID_b1b1fa7c_7304_4c64_a329_f58c0255fab6);





UUID_6a8b88ad_7d82_444a_acd6_5bda54cd21ce = new Sprite(UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b,Texture_UUID_bff3df74_a4e3_4eb5_8a30_abff758cf5e1,"UUID_6a8b88ad_7d82_444a_acd6_5bda54cd21ce");
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b->AddComponent((Component*)UUID_6a8b88ad_7d82_444a_acd6_5bda54cd21ce);


UUID_d90fec20_2a7f_4d6a_9323_585d33720a0a = new Dialogue1(UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b,1,3,new Texture(),Texture_UUID_bff3df74_a4e3_4eb5_8a30_abff758cf5e1,Texture_UUID_52f16e30_b1a8_408e_9664_d6d710303482,Texture_UUID_6cc02476_4d75_4e06_b505_3db525f0673d,"UUID_d90fec20_2a7f_4d6a_9323_585d33720a0a");
UUID_46d2d931_a923_4a86_b7dc_b8c4d180a91b->AddComponent((Component*)UUID_d90fec20_2a7f_4d6a_9323_585d33720a0a);


}

        return newScene;

    }

    Scene* GetSceneInBuild(unsigned char* name) {
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
};


void LoadScene(Scene* scene, int nb);

GameObject* FindWithName(unsigned char* name, GameObject* gameObject);

#endif