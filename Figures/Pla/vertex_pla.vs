#version 330

layout (location = 0) in vec3 position;

uniform mat4 proj;
uniform mat4 view;
uniform mat4 model;

uniform mat4 scale;

void main()
{
    gl_Position = scale * proj * view * model * vec4(position, 1.0);
}