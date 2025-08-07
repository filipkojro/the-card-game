"use client"

import React from 'react';
import {useDraggable} from '@dnd-kit/core';
import {CSS} from '@dnd-kit/utilities';

export function Draggable(props: any) {
  const {over,isDragging, attributes, listeners, setNodeRef, transform} = useDraggable({
    id: props.id,
  });
  const style = {
    transform: CSS.Translate.toString(transform),
  };
  
  const text = isDragging ? "im over " + over?.id : "id " + props.id;
  
  return (
    <button ref={setNodeRef} style={style} {...listeners} {...attributes}>
      {text}
    </button>
  );
}
