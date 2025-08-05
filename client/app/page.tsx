"use client"

import React, { useState } from 'react';
import {DndContext} from '@dnd-kit/core';

import {Draggable} from './Draggable';
import {Droppable} from './Droppable';

export default function App() {

  const [items] = useState(['1', '2', '3', '4']);


  return (
    <DndContext>
      {items.map(id => 
        <Draggable id={id} key={id}>id: {id}</Draggable>
      )}
      {/* <Draggable id='a'>Ala ma kota</Draggable>
      <Draggable id='b'>Ala ma kota</Draggable> */}
      <Droppable id={'one drop'}>Drop me here</Droppable>
      <Droppable id={'drop number two'}>Drop me here</Droppable>
    </DndContext>
  )
}