<template>
  <div class="transition-system-container flex justify-center items-center mt-8">
    <div ref="cyContainer" :style="{ width: props.width + 'px', height: props.height + 'px' }"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';
import cytoscape from 'cytoscape';

interface State {
  id: string;
  x?: number;
  y?: number;
  label?: string; // Atomic Propositions (below right)
  name?: string;  // Inside the rectangle
  initial?: boolean;
}

interface Transition {
  source: string;
  target: string;
  action?: string;
  loopDirection?: string; // e.g., '0deg', '45deg', '90deg'
  loopSweep?: string;     // e.g., '-90deg'
}

interface Props {
  states: State[];
  transitions: Transition[];
  width?: number;
  height?: number;
  auto?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  width: 600,
  height: 400,
  auto: true
});

const cyContainer = ref<HTMLElement | null>(null);
let cy: cytoscape.Core | null = null;

const render = () => {
  if (!cyContainer.value) return;

  // Prepare elements
  const elements: any[] = [];
  const rectW = 60;
  const rectH = 40;

  const hasMissingCoords = props.states.some(s => s.x === undefined || s.y === undefined);
  // Use automatic layout only if coordinates are missing.
  // If coordinates are present, we use 'preset' layout.
  const shouldLayout = hasMissingCoords;

  props.states.forEach(s => {
    // Main State Node
    const hasPosition = s.x !== undefined && s.y !== undefined;
    elements.push({
      group: 'nodes',
      data: { 
        id: s.id, 
        name: s.name || s.id 
      },
      position: hasPosition ? { x: s.x!, y: s.y! } : undefined,
      classes: 'state'
    });

    // Label Node (for propositions)
    if (s.label) {
      elements.push({
        group: 'nodes',
        data: { 
            id: s.id + '_label', 
            label: `{${s.label}}`
            // Removing parent to transform label into independent node near state
            // parent: s.id 
        },
        position: hasPosition ? { x: s.x! + 20, y: s.y! + 35 } : undefined,
        classes: 'label-node'
      });
    }

    // Initial Arrow Source
    if (s.initial) {
       elements.push({
          group: 'nodes',
          data: { id: 'init_' + s.id },
          position: hasPosition ? { x: s.x! - 50, y: s.y! } : undefined,
          classes: 'init-source'
       });
       elements.push({
          group: 'edges',
          data: { source: 'init_' + s.id, target: s.id },
          classes: 'init-edge'
       });
    }
  });

  props.transitions.forEach((t, i) => {
    elements.push({
      group: 'edges',
      data: { 
        id: 'e' + i, 
        source: t.source, 
        target: t.target, 
        action: t.action,
        loopDirection: t.loopDirection || '-45deg',
        loopSweep: t.loopSweep || '-90deg'
      }
    });
  });

  cy = cytoscape({
    container: cyContainer.value,
    elements: elements,
    style: [
      {
        selector: '.state',
        style: {
          'shape': 'round-rectangle',
          'width': rectW,
          'height': rectH,
          'background-color': '#FFF59D',
          'border-width': 2,
          'border-color': '#000',
          'content': 'data(name)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': '#000',
          'font-weight': 'bold',
          'font-size': 14
        }
      },
      {
        selector: '.label-node',
        style: {
          'shape': 'rectangle',
          'width': 1,
          'height': 1,
          'background-opacity': 0,
          'border-width': 0,
          'content': 'data(label)',
          'text-valign': 'center',
          'text-halign': 'center', // Center text at the point
          'color': '#555',
          'font-size': 12
        }
      },
      {
        selector: 'edge[loopDirection]',
        style: {
          'loop-direction': 'data(loopDirection)', 
          'loop-sweep': 'data(loopSweep)'
        }
      },
      {
        selector: 'edge', // Default style for edges
        style: {
          'width': 2,
          'line-color': '#333',
          'target-arrow-color': '#333',
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier'
          // Defaults handled by cytoscape or explicit default if needed
        }
      },
      {
        selector: 'edge[action]',
        style: {
          'label': 'data(action)',
          'font-size': 14,
          'text-rotation': 'autorotate',
          'text-background-opacity': 1,
          'text-background-color': '#ffffff',
          'text-background-padding': '2px'
        }
      },
      {
         selector: '.init-source',
         style: {
            'width': 1, 
            'height': 1, 
            'background-opacity': 0,
            'border-width': 0
         }
      },
      {
         selector: '.init-edge',
         style: {
            'width': 2,
            'line-color': '#000',
            'target-arrow-color': '#000',
            'target-arrow-shape': 'triangle',
            'curve-style': 'straight'
         }
      }
    ],
    layout: { name: 'preset' }, // Initial preset layout to place elements
    userZoomingEnabled: true,
    userPanningEnabled: true,
    boxSelectionEnabled: false
  });

  // Enable dragging even for nodes with explicit positions
  cy.nodes().grabify();

  // Export to console on right-click
  cy.on('cxttap', (event) => {
    if (event.target === cy) {
      const statesArr = props.states.map(s => {
        const node = cy?.getElementById(s.id);
        const pos = node?.position();
        return {
          ...s,
          x: Math.round(pos?.x || 0),
          y: Math.round(pos?.y || 0)
        };
      });

      const statesStr = JSON.stringify(statesArr, null, 2)
        .replace(/"([^"]+)":/g, '$1:') // remove quotes from keys
        .replace(/"/g, "'"); // use single quotes

      const transStr = JSON.stringify(props.transitions, null, 2)
        .replace(/"([^"]+)":/g, '$1:')
        .replace(/"/g, "'");

      const code = `<TransitionSystem 
  :states="${statesStr}"
  :transitions="${transStr}"
  :height="${props.height}"
/>`;
      
      console.log('--- TransitionSystem Export ---');
      console.log(code);
      console.log('-------------------------------');
      alert('Diagram code exported to console!');
    }
  });

  // Define layout configuration
  const layoutConfig = {
      name: shouldLayout ? 'cose' : 'preset',
      animate: false,
      padding: 10,
      fit: true,
      randomize: false 
  };

  // Helper to update positions
  const updateAuxiliaryNodes = () => {
      cy?.batch(() => {
          cy?.nodes('.state').forEach(node => {
              const pos = node.position();
              
              // Move Label Node
              const labelNode = cy?.getElementById(node.id() + '_label');
              if (labelNode && labelNode.nonempty()) {
                  labelNode.position({
                      x: pos.x + 20,
                      y: pos.y + 35
                  });
              }

              // Move Initial Arrow Source
              const initNode = cy?.getElementById('init_' + node.id());
              if (initNode && initNode.nonempty()) {
                  initNode.position({
                      x: pos.x - 50, // Reduced offset
                      y: pos.y
                  });
              }
          });
      });
  };

  // Bind layout signals
  cy.on('layoutstop', updateAuxiliaryNodes);

  // Run the layout explicitly
  cy.layout(layoutConfig).run();
  
  // Also run update immediately for manual layout case where layoutstop might have fired too early (unlikely if run() is called now)
  // or for initial render?
  // updateAuxiliaryNodes(); // layoutstop will handle it.
};

onMounted(() => {
  render();
});

watch(() => props, render, { deep: true });
</script>

<style scoped>
/* No extra css needed */
</style>
