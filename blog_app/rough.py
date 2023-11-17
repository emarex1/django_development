<!-- templates/base.html -->
{% load static %}
<html>
  <head>
    <title>Django blog</title>
    <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400"
      rel="stylesheet">
    <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  <body>
    <div>
      <header>
        <div class="nav-left">
          <h1><a href="{% url 'home' %}">Django blog</a></h1>
        </div>
        <div class="nav-right">
          <a href="{% url 'post_new' %}">Create New Blog</a>
        </div>
      </header>
      {% if user.is_authenticated %}
        <p>Hi {{ user.username }}!</p>
        <p><a href="{% url 'logout' %}">Log out</a></p>
      {% else %}
        <p>You are not logged in.</p>
        <a href="{% url 'login' %}">Log In</a> | 
        <a href="{% url 'signup' %}">Sign Up</a>
      {% endif %}
    {% block content %}
    {% endblock content %}
    </div>
  </body>
</html>

i applied the below css to remove the underline in create new blog above but not working
header .nav-right a {
    text-decoration: none;
  }