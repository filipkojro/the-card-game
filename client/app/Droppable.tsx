"use client"

import React from 'react';
import {useDroppable} from '@dnd-kit/core';

export function Droppable(props: any) {
  const {isOver, over, setNodeRef} = useDroppable({
    id: props.id,
  });
  const style = {
    backgroundColor:  isOver ? 'green' : 'red'
  };
  

  const test = over ? over.id : "not";
  
  return (
    <div ref={setNodeRef} style={style}>
      {test}
    </div>
  );
}
