"use client"

type UniqueIdentifier = string | number;

import React, { useState } from 'react';
import {DndContext, DragOverlay} from '@dnd-kit/core';

import {Draggable} from './Draggable';
import {Droppable} from './Droppable';

class Item {
  parent: UniqueIdentifier | null;
  id: number;
  element: any;

  constructor(parent: UniqueIdentifier | null, id: number){
    this.parent = parent;
    this.id = id
    this.element = <Draggable id={this.id}></Draggable>;
  }
}


export default function App() {

  const containers = ['A', 'B', 'C'];
  const [items] = useState([new Item('A', 0), new Item('B', 1), new Item('A', 2)]);

  const [isDragging, setIsDragging] = useState(false);


  const [activeId, setActiveId] = useState<UniqueIdentifier | null>(null);

  return (
    <DndContext onDragStart={(props) => setActiveId(props.active.id)}
                onDragEnd={({over}) => {
                  const item = items.find(item => item.id === activeId);
                  if (item) {
                    item.parent = over ? over.id : null;
                  }
                  setIsDragging(false);
                }}
                onDragCancel={() => setIsDragging(false)}
      >

      {containers.map(container_id => (
        <Droppable id={container_id} key={container_id}>
          <h1>{container_id}</h1>
          <ul>
            {items.map(item => (
              <li id={item.id.toString()} key={item.id}>
                {item.parent == container_id ? item.element : "not"}
              </li>
            ))}
          </ul>
          
        </Droppable>
      ))}

    </DndContext>

  );
}

