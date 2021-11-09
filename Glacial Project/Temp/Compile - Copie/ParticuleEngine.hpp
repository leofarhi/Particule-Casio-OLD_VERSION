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

PlayerController(GameObject* gameObject, Texture* Bas1, Texture* Bas2, Texture* Bas3, Texture* Haut1, Texture* Haut2, Texture* Haut3, Texture* Droite1, Texture* Droite2, Texture* Droite3, Texture* Gauche1, Texture* Gauche2, Texture* Gauche3, int Vitesse, const char* UUID = NULL);
    
void Update();
void Start();

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


    Scene* GetSceneInBuild(int index);

    Scene* GetSceneInBuild(unsigned char* name);
};


void LoadScene(Scene* scene, int nb);

GameObject* FindWithName(unsigned char* name, GameObject* gameObject);

#endif