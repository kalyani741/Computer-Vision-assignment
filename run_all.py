"""
Master runner script: Executes all 25 Computer Vision solutions sequentially,
verifies output generation, and displays a comprehensive test report.
"""

import os
import sys
import subprocess
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOLUTIONS_DIR = os.path.join(SCRIPT_DIR, "solutions")
OUTPUTS_DIR = os.path.join(SCRIPT_DIR, "outputs")

# Expected outputs for each question
EXPECTED_OUTPUTS = {
    "Q01": ["outputs/Q01/Q01_original_image.png"],
    "Q02": ["outputs/Q02/Q02_result.txt"],
    "Q03": ["outputs/Q03/Q03_result.txt"],
    "Q04": ["outputs/Q04/Q04_result.txt"],
    "Q05": ["outputs/Q05/Q05_result.txt"],
    "Q06": ["outputs/Q06/Q06_saved_image.png"],
    "Q07": ["outputs/Q07/Q07_grayscale.png"],
    "Q08": ["outputs/Q08/Q08_grayscale_converted.png"],
    "Q09": ["outputs/Q09/Q09_matplotlib_output.png"],
    "Q10": ["outputs/Q10/Q10_resized.png"],
    "Q11": ["outputs/Q11/Q11_result.txt"],
    "Q12": ["outputs/Q12/Q12_modified_pixel.png"],
    "Q13": ["outputs/Q13/Q13_result.txt"],
    "Q14": [
        "outputs/Q14/Q14_blue_channel.png",
        "outputs/Q14/Q14_green_channel.png",
        "outputs/Q14/Q14_red_channel.png",
    ],
    "Q15": ["outputs/Q15/Q15_merged.png"],
    "Q16": ["outputs/Q16/Q16_result.txt"],
    "Q17": ["outputs/Q17/Q17_result.txt"],
    "Q18": ["outputs/Q18/Q18_result.txt"],
    "Q19": ["outputs/Q19/Q19_constant_128.png"],
    "Q20": ["outputs/Q20/Q20_intensity_ramp.png"],
    "Q21": ["outputs/Q21/Q21_4bit_quantized.png"],
    "Q22": ["outputs/Q22/Q22_2bit_quantized.png"],
    "Q23": [
        "outputs/Q23/Q23_original.png",
        "outputs/Q23/Q23_downsampled.png",
        "outputs/Q23/Q23_resolution.txt",
    ],
    "Q24": ["outputs/Q24/Q24_roi.png"],
    "Q25": ["outputs/Q25/Q25_rotated_90.png"],
}

def main():
    print("=" * 70)
    print("Executing All 25 Computer Vision Assignment Solutions")
    print("=" * 70)

    solution_files = sorted([f for f in os.listdir(SOLUTIONS_DIR) if f.startswith("Q") and f.endswith(".py")])
    if len(solution_files) != 25:
        print(f"Warning: Found {len(solution_files)} files in solutions/ (expected 25)")

    results = []
    env = os.environ.copy()
    env["HEADLESS"] = "1"  # Avoid GUI modal blocking during automated execution

    start_time = time.time()

    for idx, sol_file in enumerate(solution_files, 1):
        q_tag = sol_file[:3]
        file_path = os.path.join(SOLUTIONS_DIR, sol_file)
        print(f"[{idx:02d}/25] Running {sol_file}...", end=" ", flush=True)

        res = subprocess.run(
            [sys.executable, file_path, "--headless"],
            cwd=SCRIPT_DIR,
            env=env,
            capture_output=True,
            text=True
        )

        success = (res.returncode == 0)

        # Verify output files
        expected = EXPECTED_OUTPUTS.get(q_tag, [])
        missing_outputs = []
        for rel_out in expected:
            full_out = os.path.join(SCRIPT_DIR, rel_out)
            if not os.path.exists(full_out) or os.path.getsize(full_out) == 0:
                missing_outputs.append(rel_out)

        if success and not missing_outputs:
            print("OK [PASSED]")
            results.append((q_tag, sol_file, "PASSED", ""))
        else:
            status = "FAILED" if not success else "MISSING OUTPUTS"
            err_msg = res.stderr.strip() or f"Missing: {missing_outputs}"
            print(f"{status} (Details: {err_msg[:60]}...)")
            results.append((q_tag, sol_file, status, err_msg))

    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print(f"SUMMARY: 25 Solutions Executed in {elapsed:.2f} seconds")
    print("=" * 70)
    print(f"{'Question':<10} {'File':<30} {'Status':<15}")
    print("-" * 70)

    passed_count = 0
    for q_tag, filename, status, err in results:
        print(f"{q_tag:<10} {filename:<30} {status:<15}")
        if status == "PASSED":
            passed_count += 1

    print("-" * 70)
    print(f"Total Passed: {passed_count} / {len(solution_files)}")
    if passed_count == 25:
        print("ALL 25 QUESTIONS COMPLETED AND VERIFIED SUCCESSFULLY!")
    else:
        print(f"ATTENTION: {25 - passed_count} questions had issues.")
        sys.exit(1)

if __name__ == "__main__":
    main()
