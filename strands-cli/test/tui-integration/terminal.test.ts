import { describe, expect, it } from 'vitest'

import { TUI_CASE } from './catalog.js'
import { expectRestoredTerminal, runTuiScenario } from './harness.js'

describe('TUI terminal integration', () => {
  it(TUI_CASE.resize.testName, async () => {
    const result = await runTuiScenario(TUI_CASE.resize.scenario)

    expect(result.returnCode).toBe(0)
    expect(result.resizeOutput.split('\u001b[1;1H')).toHaveLength(7)
    // Native resize events may be coalesced or delivered individually by the OS.
    const burstRedraws = result.resizeBurstOutput.split('\u001b[1;1H').length - 1
    expect(burstRedraws).toBeGreaterThanOrEqual(1)
    expect(burstRedraws).toBeLessThanOrEqual(3)
    expect(result.resizeNoopOutput).toBe('')
    for (const code of ['2J', '3J', '2K']) {
      expect(result.resizeOutput + result.resizeBurstOutput).not.toContain(`\u001b[${code}`)
    }
    expectRestoredTerminal(result)
  })

  it(TUI_CASE.exit.testName, async () => {
    const result = await runTuiScenario(TUI_CASE.exit.scenario)

    expect(result.returnCode).toBe(0)
    expectRestoredTerminal(result)
    const resumeMessage = 'Resume with: strands --session-id fixture-session'
    expect(result.output.split(resumeMessage)).toHaveLength(2)
    expect(result.output.indexOf('\u001b[?1049l')).toBeLessThan(result.output.indexOf(resumeMessage))
  })
})
