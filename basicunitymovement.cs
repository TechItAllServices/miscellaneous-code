// NOTE: Not tested. Report any issues here: https://github.com/TechItAllServices/miscellaneous-code/issues
using UnityEngine;

public class basicunitymovement : MonoBehaviour
{
    public float speed = 5f;

    void Update()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        Vector3 direction = new Vector3(horizontalInput, 0, verticalInput);

        transform.Translate(direction * speed * Time.deltaTime);
    }
}

