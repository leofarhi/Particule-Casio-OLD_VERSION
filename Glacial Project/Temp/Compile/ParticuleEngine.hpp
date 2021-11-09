#pragma once
#ifndef ClassParticuleEngine
#define ClassParticuleEngine
#include "Announcement.h"
#include "MonochromeLib.h"
#include "List.h"
#include <iostream>
#include <math.h>
#include "usefull.h"
#include "Ressources.h"

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

class Quaternion {
    //https://docs.unity3d.com/ScriptReference/Quaternion.html
public:

};

class Matrix4x4 {
    //https://docs.unity3d.com/ScriptReference/Matrix4x4.html
public:

};

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
    virtual void DestroyImmediate() {}
    virtual void DontDestroyOnLoad() {}
    virtual void FindObjectOfType() {}
    virtual void FindObjectsOfType() {}
    virtual void Instantiate() {}

    // Overload operator
    bool operator==(const Object& obj);

    bool operator!=(const Object& obj);
private:
    unsigned char* ID;
};

class Component : public Object {
    //https://docs.unity3d.com/ScriptReference/Component.html
public:
    char* tag;
    GameObject* gameObject;
    Transform* transform;

    Component(const char* name, GameObject* gameObject, const char* UUID = NULL);

    ~Component();

    void BroadcastMessage();
    void CompareTag();
    void GetComponent();
    void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void TryGetComponent();

    virtual void Awake() {}
    virtual void FixedUpdate() {}
    virtual void LateUpdate() {}
    virtual void OnAnimatorIK() {}
    virtual void OnAnimatorMove() {}
    virtual void OnApplicationFocus() {}
    virtual void OnApplicationPause() {}
    virtual void OnApplicationQuit() {}
    virtual void OnAudioFilterRead() {}
    virtual void OnBecameInvisible() {}
    virtual void OnBecameVisible() {}
    virtual void OnCollisionEnter() {}
    virtual void OnCollisionEnter2D() {}
    virtual void OnCollisionExit() {}
    virtual void OnCollisionExit2D() {}
    virtual void OnCollisionStay() {}
    virtual void OnCollisionStay2D() {}
    virtual void OnConnectedToServer() {}
    virtual void OnControllerColliderHit() {}
    virtual void OnDestroy() {}
    virtual void OnDisable() {}
    virtual void OnDisconnectedFromServer() {}
    virtual void OnDrawGizmos() {}
    virtual void OnDrawGizmosSelected() {}
    virtual void OnEnable() {}
    virtual void OnFailedToConnect() {}
    virtual void OnFailedToConnectToMasterServer() {}
    virtual void OnGUI() {}
    virtual void OnJointBreak() {}
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
    virtual void OnRenderImage() {}
    virtual void OnRenderObject() {}
    virtual void OnSerializeNetworkView() {}
    virtual void OnServerInitialized() {}
    virtual void OnTransformChildrenChanged() {}
    virtual void OnTransformParentChanged() {}
    virtual void OnTriggerEnter() {}
    virtual void OnTriggerEnter2D() {}
    virtual void OnTriggerExit() {}
    virtual void OnTriggerExit2D() {}
    virtual void OnTriggerStay() {}
    virtual void OnTriggerStay2D() {}
    virtual void OnValidate() {}
    virtual void OnWillRenderObject() {}
    virtual void Reset() {}
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
    Vector2* localScale;
    //Matrix4x4* localToWorldMatrix;
    Vector2* lossyScale;
    Transform* parent;
    Vector2* position;
    //Vector2* right;
    Transform* root;
    //Quaternion* rotation;
    //Vector2* up;
    //Matrix4x4* worldToLocalMatrix;

    Transform(GameObject* gameObject, const char* UUID = NULL, const char* name = "Transform");

    ~Transform();

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

    void CancelInvoke();
    void Invoke();
    void InvokeRepeating();
    void IsInvoking();
    void StartCoroutine();
    void StopAllCoroutines();
    void StopCoroutine();
    //print c'est pour l'éditeur donc il n'est pas présent
};


class GameObject : public Object {
    //https://docs.unity3d.com/ScriptReference/GameObject.html
private:
    List<Component*> ListOfComponent;
public:
    bool activeInHierarchy;
    bool activeSelf;
    bool isStatic;
    Layer layer;
    Scene* scene;
    long sceneCullingMask;
    Tag tag;
    Transform* transform;

    GameObject(Scene* scene, const char* name, const char* UUID = NULL);

    ~GameObject();

    bool IsActive();

    void Update();

    void Start();

    void AddComponent(Component* component);
    void BroadcastMessage();
    void CompareTag();
    Component* GetComponent(const char* name);
    void GetComponentInChildren();
    void GetComponentInParent();
    void GetComponents();
    void GetComponentsInChildren();
    void GetComponentsInParent();
    void SendMessage();
    void SendMessageUpwards();
    void SetActive();
    void TryGetComponent();

    static void CreatePrimitive();
    GameObject* Find(unsigned char* name);
    static void FindGameObjectsWithTag();
    static void FindWithTag();
};


class Scene {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.Scene.html
public:
    List<GameObject*> AllGameObject;
    SceneManager* sceneManager;
    void GetRootGameObjects();
    bool IsValid();

    void AddGameObject(GameObject* gObj);

    void Update();

    void Start();

    int buildIndex;
    bool isDirty;
    bool isLoaded;
    char* name;
    //char* path;
    int rootCount;

    List<Camera*> AllCameras;
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

    void Update();
};

class Sprite : MonoBehaviour { //: public VisualElement {
    //https://docs.unity3d.com/ScriptReference/UIElements.Image.html
public:

    Texture* image;


    Sprite(GameObject* gameObject, Texture* image, const char* UUID = NULL);

    void Update();
};


class Rigidbody : MonoBehaviour {
private:
    
public:
    float Mass;
    bool UseGravity;
    bool IsKinematic;
    Vector2* velocity;

    Rigidbody(GameObject* gameObject, float Mass, bool UseGravity, bool IsKinematic, const char* UUID = NULL);

    ~Rigidbody();

    void Start();
    
};


class Collider2D : MonoBehaviour {
    //https://docs.unity3d.com/ScriptReference/Collider2D.html
public:
    
};

class BoxCollider2D : Collider2D {
    //https://docs.unity3d.com/ScriptReference/BoxCollider2D.html
public:
    
};

class Text : MonoBehaviour {

public:
    unsigned char* text;

    Text(GameObject* gameObject, unsigned char* text, const char* UUID = NULL);

    void Update();


};

class Tilemap : MonoBehaviour { 
public:

    Texture** images;
    int* Datas;
    Vector2* sizeTilemap;
    Vector2* sizeCase;


    Tilemap(GameObject* gameObject, Vector2* sizeTilemap, Vector2* sizeCase, const char* UUID = NULL);

    ~Tilemap();

    void Update();
};


class PlayerController : MonoBehaviour {
private:
    int Frame;

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
ML_rectangle((127 / 2) - (12 / 2), (63 / 2) - (20 / 2), (127 / 2) + (12 / 2), (63 / 2) - (20 / 2) +20, 0, ML_WHITE, ML_WHITE);
if (IsKeyDown(KEY_CTRL_UP)){
this->gameObject->transform->position->y += ((0)-(this->Vitesse));
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Haut1;

}else {
if (((this->Frame)==(1))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Haut2;

}else {
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Haut3;

}

}

}else {
if (IsKeyDown(KEY_CTRL_DOWN)){
this->gameObject->transform->position->y += this->Vitesse;
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Bas1;

}else {
if (((this->Frame)==(1))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Bas2;

}else {
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Bas3;

}

}

}else {
if (IsKeyDown(KEY_CTRL_RIGHT)){
this->gameObject->transform->position->x += this->Vitesse;
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Droite1;

}else {
if (((this->Frame)==(1))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Droite2;

}else {
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Droite3;

}

}

}else {
if (IsKeyDown(KEY_CTRL_LEFT)){
this->gameObject->transform->position->x += ((0)-(this->Vitesse));
if (((((this->Frame)==(0)))||(((this->Frame)==(2))))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Gauche1;

}else {
if (((this->Frame)==(1))){
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Gauche2;

}else {
((Sprite*)this->gameObject->GetComponent("Sprite"))->image =this->Gauche3;

}

}

}

}

}

}
this->Frame=mod((int)((this->Frame)+(1)),(int)4);
gameObject->scene->AllCameras[0]->gameObject->transform->position->Set(*gameObject->transform->position-*(new Vector2(127/2,63/2))+ *(new Vector2(16 / 2, 20 / 2)));

}
void Start(){
this->Frame=0;

}

};


class SceneManager {
    //https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.html
public:
    int sceneCount;
    static int sceneCountInBuildSettings;

    //Static Methods
    static void CreateScene();
    static void GetActiveScene();
    static void GetSceneAt();
    static void GetSceneByBuildIndex();
    static void GetSceneByName();
    static void GetSceneByPath();
    void LoadScene(int index);
    void LoadScene(unsigned char* name);
    static void LoadSceneAsync();
    static void MergeScenes();
    static void MoveGameObjectToScene();
    static void SetActiveScene();
    static void UnloadSceneAsync();

    GameObject* FindWithName(unsigned char* name);

    //Events
    static void activeSceneChanged();
    static void sceneLoaded();
    static void sceneUnloaded();

    void UpdateScene();

    void StartScene();
private:
    List<Scene*> AllSceneLoaded;


    Scene* GetSceneInBuild(int index) {
        Scene* newScene = new Scene();
        newScene->sceneManager = this;

        Texture* Texture_UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c= new Texture("Texture",16,20,UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c);
Texture* Texture_UUID_3b28f421_9575_4c12_91c4_2c145b435538= new Texture("Texture",16,20,UUID_3b28f421_9575_4c12_91c4_2c145b435538);
Texture* Texture_UUID_53848287_45f6_410e_b7f2_b01019c5a1e9= new Texture("Texture",16,20,UUID_53848287_45f6_410e_b7f2_b01019c5a1e9);
Texture* Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af= new Texture("Texture",16,20,UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af);
Texture* Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea= new Texture("Texture",16,20,UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea);
Texture* Texture_UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae= new Texture("Texture",16,20,UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae);
Texture* Texture_UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b= new Texture("Texture",16,20,UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b);
Texture* Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6= new Texture("Texture",16,20,UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6);
Texture* Texture_UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f= new Texture("Texture",16,20,UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f);
Texture* Texture_UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f= new Texture("Texture",16,20,UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f);
Texture* Texture_UUID_e870f483_8f84_44ae_b86c_bb1978372306= new Texture("Texture",16,20,UUID_e870f483_8f84_44ae_b86c_bb1978372306);
Texture* Texture_UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6= new Texture("Texture",16,20,UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6);
if (index == 0){
GameObject* UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46;
GameObject* UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca;
GameObject* UUID_400c4826_db9d_4390_963a_d132c010b431;
Sprite* UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3;
PlayerController* UUID_6640de22_b0db_4537_8522_f3a7a703d68f;

Tilemap* UUID_fbe0964f_80f0_4bb3_9701_3928fd378215;

Camera* UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4;

UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46= new GameObject(newScene, "Camera","UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46");
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->activeSelf = true;
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->activeInHierarchy = true;
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->isStatic = false;
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->transform->position->Set(0,0);
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46);
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca= new GameObject(newScene, "Tilemap","UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca");
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->activeSelf = true;
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->activeInHierarchy = true;
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->isStatic = false;
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->transform->position->Set(0,0);
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->transform->localPosition->Set(0,0);
newScene->AddGameObject(UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca);
UUID_400c4826_db9d_4390_963a_d132c010b431= new GameObject(newScene, "Player","UUID_400c4826_db9d_4390_963a_d132c010b431");
UUID_400c4826_db9d_4390_963a_d132c010b431->activeSelf = true;
UUID_400c4826_db9d_4390_963a_d132c010b431->activeInHierarchy = true;
UUID_400c4826_db9d_4390_963a_d132c010b431->isStatic = false;
UUID_400c4826_db9d_4390_963a_d132c010b431->transform->position->Set(40.0,20.0);
UUID_400c4826_db9d_4390_963a_d132c010b431->transform->localPosition->Set(40.0,20.0);
newScene->AddGameObject(UUID_400c4826_db9d_4390_963a_d132c010b431);




UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4 = new Camera(UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46,"UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4");
UUID_7f4f5e06_f8a9_41f1_b9f9_dae0dba98d46->AddComponent((Component*)UUID_73ea44a9_6256_47d4_be2b_b37bb79f0ba4);





UUID_fbe0964f_80f0_4bb3_9701_3928fd378215 = new Tilemap(UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca,new Vector2(20,20),new Vector2(16,16),"UUID_fbe0964f_80f0_4bb3_9701_3928fd378215");
UUID_131a6cdf_9eb2_4aa9_a1a7_af674e8990ca->AddComponent((Component*)UUID_fbe0964f_80f0_4bb3_9701_3928fd378215);
static int UUID_fbe0964f_80f0_4bb3_9701_3928fd378215_TilemapDatas[] = {1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->Datas = UUID_fbe0964f_80f0_4bb3_9701_3928fd378215_TilemapDatas;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images = new Texture * [3];
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[0] = new Texture();
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[1] = Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af;
UUID_fbe0964f_80f0_4bb3_9701_3928fd378215->images[2] = Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6;





UUID_6640de22_b0db_4537_8522_f3a7a703d68f = new PlayerController(UUID_400c4826_db9d_4390_963a_d132c010b431,Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea,Texture_UUID_53848287_45f6_410e_b7f2_b01019c5a1e9,Texture_UUID_3b28f421_9575_4c12_91c4_2c145b435538,Texture_UUID_e870f483_8f84_44ae_b86c_bb1978372306,Texture_UUID_355aae99_e49f_4a07_b7b8_ecf7673e547c,Texture_UUID_9b63aa6b_0684_4171_a80a_a82e6e29f6ae,Texture_UUID_600cd8e3_41c3_4a5e_8550_1ef2c44147af,Texture_UUID_f018f68e_6f34_4b9a_bbc4_9513b3bc17c6,Texture_UUID_dc9afec8_2e2e_4996_8271_1ac4cb193c2f,Texture_UUID_e4cf6d14_c9f2_4336_bb03_53529e5e4d6f,Texture_UUID_a1bc752c_94cf_41b4_a8f3_a32ec3d9312b,Texture_UUID_a9e4b5ab_ecdd_4525_8dbd_dbfaef28a6f6,5,"UUID_6640de22_b0db_4537_8522_f3a7a703d68f");
UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_6640de22_b0db_4537_8522_f3a7a703d68f);


UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3 = new Sprite(UUID_400c4826_db9d_4390_963a_d132c010b431,Texture_UUID_6432dbba_ba4c_4f25_a9d3_15cf97c6e1ea,"UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3");
UUID_400c4826_db9d_4390_963a_d132c010b431->AddComponent((Component*)UUID_43fd50a2_fd6b_402d_ab19_3ccb56f74fc3);


}

        return newScene;

    }

    Scene* GetSceneInBuild(unsigned char* name);
};


void LoadScene(Scene* scene, int nb);

GameObject* FindWithName(unsigned char* name, GameObject* gameObject);

#endif