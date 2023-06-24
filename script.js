import * as THREE from "./three.module.js";
import { OrbitControls } from './orbitcontrols.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );

const renderer = new THREE.WebGLRenderer({alpha: true});
renderer.setSize( window.innerWidth, window.innerHeight );
renderer.shadowMap.enabled = true;
document.body.appendChild( renderer.domElement );

const controls = new OrbitControls(camera, renderer.domElement );
controls.target = new THREE.Vector3(0, 0, 0);


const geometry = new THREE.BoxGeometry(20, 20, 32, 32);
const material = new THREE.MeshStandardMaterial({ color: 0xff0000 })
const cube1 = new THREE.Mesh(geometry, material);
const cube2 = new THREE.Mesh(geometry, material);
cube2.color = new THREE.Color(0xff0000);
cube2.receiveShadow = false;
const cube3 = new THREE.Mesh(geometry, material);
const cube4 = new THREE.Mesh(geometry, material);
const cube5 = new THREE.Mesh(geometry, material);
const cube6 = new THREE.Mesh(geometry, material);
const cube7 = new THREE.Mesh(geometry, material);
const cube8 = new THREE.Mesh(geometry, material);
const cube9 = new THREE.Mesh(geometry, material);
const cube10 = new THREE.Mesh(geometry, material);
const cube11 = new THREE.Mesh(geometry, material);
const cube12 = new THREE.Mesh(geometry, material);
const cube13 = new THREE.Mesh(geometry, material);
const cube14 = new THREE.Mesh(geometry, material);
const cube15 = new THREE.Mesh(geometry, material);
const cube16 = new THREE.Mesh(geometry, material);
const cube17 = new THREE.Mesh(geometry, material);
const cube18 = new THREE.Mesh(geometry, material);
const cube19 = new THREE.Mesh(geometry, material);
const cube20 = new THREE.Mesh(geometry, material);
const cube21 = new THREE.Mesh(geometry, material);
const cube22 = new THREE.Mesh(geometry, material);
const cube23 = new THREE.Mesh(geometry, material);
const cube24 = new THREE.Mesh(geometry, material);
const cube25 = new THREE.Mesh(geometry, material);
const cube26 = new THREE.Mesh(geometry, material);
const cube27 = new THREE.Mesh(geometry, material);
//cubes position in x
const pos_x = [
    cube1.position.x = 0,
    cube2.position.x = 20,
    cube3.position.x = -20,
    cube4.position.x = 0,
    cube5.position.x = 20,
    cube6.position.x = -20,
    cube7.position.x = 0,
    cube8.position.x = 20,
    cube9.position.x = -20,
    cube10.position.x = 0,
    cube11.position.x = 20,
    cube12.position.x = -20,
    cube13.position.x = 0,
    cube14.position.x = 20,
    cube15.position.x = -20,
    cube16.position.x = 0,
    cube17.position.x = 20,
    cube18.position.x = -20,
    cube19.position.x = 0,
    cube20.position.x = 20,
    cube21.position.x = -20,
    cube22.position.x = 0,
    cube23.position.x = 20,
    cube24.position.x = -20,
    cube25.position.x = 0,
    cube26.position.x = 20,
    cube27.position.x = -20
]

console.log(pos_x);

for (let every in pos_x) {
    if (cube1.position.x === 20) {
        every.position.x = 50
    } else if (every.position.x === -20) {
        every.position.x = -50
    }
}

//cubes position in y
cube1.position.y = 0
cube2.position.y = 0
cube3.position.y = 0
cube4.position.y = 20
cube5.position.y = 20
cube6.position.y = 20
cube7.position.y = -20
cube8.position.y = -20
cube9.position.y = -20
cube10.position.y = 0
cube11.position.y = 0
cube12.position.y = 0
cube13.position.y = 20
cube14.position.y = 20
cube15.position.y = 20
cube16.position.y = -20
cube17.position.y = -20
cube18.position.y = -20
cube19.position.y = 0
cube20.position.y = 0
cube21.position.y = 0
cube22.position.y = 20
cube23.position.y = 20
cube24.position.y = 20
cube25.position.y = -20
cube26.position.y = -20
cube27.position.y = -20
//cubes position in z
cube1.position.z = 0
cube2.position.z = 0
cube3.position.z = 0
cube4.position.z = 0
cube5.position.z = 0
cube6.position.z = 0
cube7.position.z = 0
cube8.position.z = 0
cube9.position.z = 0
cube10.position.z = 20
cube11.position.z = 20
cube12.position.z = 20
cube13.position.z = 20
cube14.position.z = 20
cube15.position.z = 20
cube16.position.z = 20
cube17.position.z = 20
cube18.position.z = 20
cube19.position.z = -20
cube20.position.z = -20
cube21.position.z = -20
cube22.position.z = -20
cube23.position.z = -20
cube24.position.z = -20
cube25.position.z = -20
cube26.position.z = -20
cube27.position.z = -20


const planeGeometry = new THREE.PlaneGeometry();
const planeMaterial = new THREE.MeshStandardMaterial({color: 0x808080});
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.receiveShadow = true;
plane.position.set(0,0,0);

const light = new THREE.DirectionalLight(0xffffff, 1, 100);
light.castShadow = true;
light.position.set(50, 0, 0);

scene.add( cube1, cube2, cube3, cube4, cube5, cube6, cube7, cube8, cube9, cube10, cube11, cube12,
     cube13, cube14, cube15, cube16, cube17, cube18, cube19, cube20, cube21, cube22, cube23, cube24,
      cube25, cube26, cube27, plane, light );
camera.position.x = 200;
camera.position.z = 400;
camera.position.y = 100;

const x_button = document.getElementById("x")
const y_button = document.getElementById("y")
const z_button = document.getElementById("z")
const x__button = document.getElementById("-x")
const y__button = document.getElementById("-y")
const z__button = document.getElementById("-z")

x_button.addEventListener("click", function() {
    camera.position.x += 20
})
y_button.addEventListener("click", function() {
    camera.position.y += 20
})
z_button.addEventListener("click", function() {
    camera.position.z += 20
})
x__button.addEventListener("click", function() {
    camera.position.x -= 20
})
y__button.addEventListener("click", function() {
    camera.position.y -= 20
})
z__button.addEventListener("click", function() {
    camera.position.z -= 20
})

function animate() {
    requestAnimationFrame( animate );
    
    renderer.render(scene, camera);
}

animate();