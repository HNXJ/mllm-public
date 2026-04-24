# mllm-telemetry-bridge
Injects real-time stats from `MLLM-Monitor` (Port 8081) into `index.html` as interactive charts.

## Protocol
1.  **Fetch:** Query `http://localhost:8081/stats` for current pipeline status (VRAM, Heartbeat, Agent Progress).
2.  **Injection:** Find `<div id="telemetry">` in `index.html`.
3.  **Visualization:** Generate Chart.js or D3.js script blocks to render the fetched data.
4.  **Real-time:** Ensure the bridge sets up an `EventSource` or periodic fetch loop in the client-side JS.
