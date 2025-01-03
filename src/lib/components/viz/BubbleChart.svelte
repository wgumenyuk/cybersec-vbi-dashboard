<script lang="ts">
    import * as d3 from "d3";

    // Dataset
    import data from "$lib/data/breaches_symbols.json";

    // Extend SimulationNodeDatum to include custom properties
    interface BubbleNode extends d3.SimulationNodeDatum {
        type: string;
        average: number;
        radius: number;
        x: number;
        y: number;
    }

    // Process data to calculate average people affected by breach type
    const bubbleData = (() => {
        const impacts: Record<string, number[]> = {};

        data.forEach((d) => {
            if (!d || typeof d !== "object") return;

            const affected = parseFloat(String(d["Affected"]));
            const types = d.Type;

            if (!isNaN(affected) && affected > 0) {
                if (Array.isArray(types)) {
                    types.forEach((type) => {
                        if (type && typeof type === "string") {
                            if (!impacts[type]) impacts[type] = [];
                            impacts[type].push(affected);
                        }
                    });
                }
            }
        });

        return Object.entries(impacts)
            .map(([type, values]) => ({
                type,
                average: values.reduce((acc, cur) => acc + cur, 0) / values.length,
            }))
            .filter(({ average }) => !isNaN(average) && average > 0);
    })();

    let svg;
    const margin = { top: 40, right: 20, bottom: 80, left: 20 };
    const width = 800 - margin.left - margin.right;
    const height = 600 - margin.top - margin.bottom;
    let tooltip = { visible: false, x: 0, y: 0, text: "", color: "" };

    // Scales for radius and color
    const r = d3
        .scaleSqrt()
        .domain([0, d3.max(bubbleData, (d) => d.average) || 0])
        .range([20, 100]); // Bubble size range

    const color = d3.scaleOrdinal(d3.schemeTableau10);

    // Force simulation for bubble layout
    let nodes: BubbleNode[] = bubbleData.map((d) => ({
        ...d,
        radius: r(d.average),
        x: Math.random() * width,
        y: Math.random() * height,
    }));

    const simulation = d3
        .forceSimulation<BubbleNode>(nodes)
        .force("x", d3.forceX(width / 2).strength(0.05))
        .force("y", d3.forceY(height / 2).strength(0.05))
        .force(
            "collision",
            d3.forceCollide<BubbleNode>().radius((d: BubbleNode) => d.radius + 5) // Add margin between bubbles
        )
        .on("tick", () => {
            // Ensures simulation updates are reflected
            simulation.stop();
        });

    function showTooltip(event: MouseEvent, type: string, average: number, bubbleColor: string) {
        tooltip = {
            visible: true,
            x: event.pageX,
            y: event.pageY - 40,
            text: `${type}: ${average.toLocaleString()} affected`,
            color: bubbleColor,
        };
    }

    function hideTooltip() {
        tooltip.visible = false;
    }

</script>

<svg
    class="w-full h-full"
    bind:this={svg}
    viewBox={`0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`}
>
    <g transform={`translate(${margin.left},${margin.top})`}>
        {#if nodes && nodes.length > 0}
            {#each nodes as { type, average, x, y, radius }}
                <circle
                    role="graphics-symbol"
                    aria-label={`Bubble for ${type}, average affected: ${average.toLocaleString()} people`}
                    cx={x}
                    cy={y}
                    r={radius}
                    fill={color(type)}
                    class="cursor-pointer opacity-80 hover:opacity-100 transition-opacity"
                    on:mouseenter={(e) => showTooltip(e, type, average, color(type))}
                    on:mouseleave={hideTooltip}
                ></circle>

                <!-- Labels near bubbles -->
                <text
                    x={x + radius / 2}
                    y={y - radius / 2}
                    text-anchor="middle"
                    class="fill-white font-bold text-sm"
                >
                    {type}
                </text>
            {/each}
        {:else}
            <text
                x={width / 2}
                y={height / 2}
                text-anchor="middle"
                class="fill-white font-bold text-base"
            >
                No data available
            </text>
        {/if}
    </g>
</svg>

<!-- Tooltip -->
{#if tooltip.visible}
    <div
        class="absolute bg-gray-800 text-white p-2 rounded shadow"
        style="top: {tooltip.y}px; left: {tooltip.x}px"
    >
        <div class="flex items-center gap-2">
            <div
                class="w-4 h-4 rounded"
                style="background-color: {tooltip.color}"
            ></div>
            <span>{tooltip.text}</span>
        </div>
    </div>
{/if}

<style>
    text {
        font-size: 14px;
        font-family: sans-serif;
        fill: white;
    }

    .fill-white {
        fill: white;
    }

    .font-bold {
        font-weight: bold;
    }

    .cursor-pointer {
        cursor: pointer;
    }

    .opacity-80 {
        opacity: 0.8;
    }

    .hover\:opacity-100:hover {
        opacity: 1;
    }

    .transition-opacity {
        transition: opacity 0.2s ease-in-out;
    }

    .absolute {
        position: absolute;
    }

    .bg-gray-800 {
        background-color: #2d3748;
    }

    .text-white {
        color: white;
    }

    .rounded {
        border-radius: 0.25rem;
    }

    .shadow {
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
</style>
