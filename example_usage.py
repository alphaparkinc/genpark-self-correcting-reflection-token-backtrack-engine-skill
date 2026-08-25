from client import SelfCorrectingReflectionTokenBacktrackEngineClient

def main():
    client = SelfCorrectingReflectionTokenBacktrackEngineClient()
    res = client.execute_reflective_reasoning_cycle('Verify asymptotic convergence of Lyapunov function for coupled non-linear oscillators')
    print('Reflection Run: ' + res['reflection_run_id'] + ' (' + str(res['reflection_tokens_generated']) + ' reflection tokens)')
    print('Self-Corrected Hallucinations: ' + str(res['detected_hallucinations_self_corrected']) + ' (Backtracks: ' + str(res['backtrack_steps_executed']) + ')')
    print('Pass Rate: ' + str(res['mathematical_derivation_pass_rate_pct']) + '% | Solution Ready: ' + str(res['final_verified_solution_ready']))

if __name__ == '__main__':
    main()
