<!DOCTYPE html>
<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>
        <H1>States</H1>
        <UL>
		{% for state in states|sort(attribute='name') %}
			<lI>{{ state.id }}: <B>{{ state.name }}</B></lI>
			  <UL>
				{% for city in state.cities|sort(attribute='name') %}
					<lI>{{ city.id }}: <B>{{city.name}}</B></LI>
				{% endfor %}
			  </UL>
		{% endfor %}
	</UL>
    </BODY>
</HTML>
