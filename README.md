# Aplicación de información geográfica

Suponga que usted hace parte del equipo que desarrolla una aplicación que trabaja con información geográfica, la cual está estructurada como un enorme grafo. Cada nodo del grafo puede representar una entidad compleja como una ciudad, pero también elementos más granulares como una industria o un lugar de turismo, etc. Los nodos están conectados con otros nodos si existe un camino entre los objetos en el mundo real.

La estructura del grafo representa cada tipo de nodo con su propia clase, mientras que cada nodo es un objeto.

A usted le ponen la tarea de implementar una funcionalidad para exportar el grafo en formato XML.

Para efectos de simplicidad, suponga que el diseño original de la estructura del grafo es el siguiente:


<div align="center">
    <img src="./images/modelo grafo.png" width="800">
</div>

Fase 1

En una primera fase, un compañero del equipo le sugiere que la solución es muy simple, ya que se puede definir la funcionalidad de exportar en cada clase y, luego, valerse de la estructura del grafo para recorrer cada nodo del grafo, ejecutando dicha funcionalidad. Esa sería una solución en la que, gracias al polimorfismo, no se estaría acoplando el código que llama al método de exportar con las clases concretas de los nodos.

Fase 2

Luego de diseñar la solución de la fase 1, el arquitecto de la aplicación le dice que no está de acuerdo con el diseño porque él no quiere alterar el código existente de las clases que representan cada tipo de nodo. Su argumento es que el código ya está en producción y él no se quiere arriesgar a dañar la aplicación por un bug potencial que se pueda introducir con los cambios que usted propone.

Además, el arquitecto cuestiona el diseño propuesto en relación a si tendría sentido tener el código de la lógica de exportación a XML dentro de las clases de los nodos. Esto debido a que la responsabilidad principal de dichas clases es trabajar con datos geográficos, y el comportamiento para exportar a XML violaría su cohesión.

Finalmente, el arquitecto expone otra razón para rechazar el diseño. Es altamente probable que después de que esta nueva funcionalidad sea implementada, alguien de mercadeo pidiera que se agregara la habilidad para exportar a un formato diferente o alguna otra cosa rara. Esto forzaría a cambiar nuevamente sus frágiles y preciadas clases de nodos.

Sin embargo, el arquitecto no es una persona cerrada y entiende que probablemente se requiera cambiar algo de las clases nodos. Por lo tanto, él le pide que diseñe una solución que implique que los cambios a las clases nodos sean mínimos y triviales y que dichos cambios permitan adicionar nuevos comportamientos sin alterar nuevamente el código.

## Diagrama de clases UML con el diseño de la solución

<div align="center">
    <img src="./images/modelo grafo sugerido.png" width="800">
</div>