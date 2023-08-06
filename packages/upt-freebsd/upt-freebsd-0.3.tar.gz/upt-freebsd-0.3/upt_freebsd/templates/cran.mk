{% extends 'base.mk' %}

{% block pkgnameprefix %}
{% endblock %}

{% block use %}
USES=		cran:auto-plist
{% endblock %}
